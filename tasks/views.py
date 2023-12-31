from datetime import timezone

from django.contrib.auth import logout
from django.db.models import Q
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseForbidden
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, DeleteView, UpdateView
from django.contrib.auth.views import LoginView

from tasks.filters import TaskFilter
from tasks.forms import TaskCreateModelForm
from tasks.models import Task
from django.contrib.auth.mixins import LoginRequiredMixin

class LocalLoginRequiredMixin(LoginRequiredMixin):
    login_url = 'auth'

class TaskCreate(LocalLoginRequiredMixin, CreateView):
    model = Task
    form_class = TaskCreateModelForm
    def form_valid(self, form):
        form.instance.user_from = self.request.user
        return super().form_valid(form)

class TaskList(LocalLoginRequiredMixin, ListView):
    model = Task
    queryset = Task.objects.all()
    def get_context_data(self, *, object_list=None, **kwargs):
        res = super().get_context_data(object_list=None, **kwargs)
        res.update({"user_name": self.request.user.username})
        res['form']=self.filterset.form
        return res
    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.filter(Q(user_to=self.request.user) | Q(user_from=self.request.user)).order_by('-date_create')
        self.filterset = TaskFilter(self.request.GET,queryset=queryset)
        return self.filterset.qs

class AuthView(LoginView):
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse_lazy('cabinet')

    def form_invalid(self, form):
        return self.render_to_response(self.get_context_data(form=form))

class DeleteTaskView(LocalLoginRequiredMixin, DeleteView):
    model = Task
    success_url = reverse_lazy('cabinet')

    def post(self, request, *args, **kwargs):
        pk = kwargs.get('pk')
        user = request.user

        try:
            Task.objects.get(Q(Q(user_from=user) | Q(user_to=user)), pk=pk)
            return super().post(request, *args, **kwargs)
        except Task.DoesNotExist:
            return HttpResponseForbidden()

class UpadateStatusView(LocalLoginRequiredMixin, UpdateView):
    model = Task
    fields = ["current_status"]
    template_name_suffix = "_update_form"
    def post(self, request, *args, **kwargs):
        pk = kwargs.get('pk')
        user = request.user

        try:
            Task.objects.get(Q(Q(user_from=user) | Q(user_to=user)), pk=pk)
            return super().post(request, *args, **kwargs)
        except Task.DoesNotExist:
            return HttpResponseForbidden()

# Create your views here.
def auth(request):
    return render(request,"Auth.html")

def logout_view(request):
    logout(request)
    return redirect('auth')

def cabinet(request):
    return HttpResponse('cabinet')

def new_task(request):
    return render(request,"New_task.html")