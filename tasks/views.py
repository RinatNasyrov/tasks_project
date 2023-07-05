from django.db.models import Q
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseForbidden
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, DeleteView, UpdateView
from django.contrib.auth.views import LoginView
from tasks.models import Task
from django.contrib.auth.mixins import LoginRequiredMixin

class TaskCreate(LoginRequiredMixin, CreateView):
    model = Task
    fields = ["description", "current_status", "user_to"]
    
    def form_valid(self, form):
        form.instance.user_from = self.request.user
        return super().form_valid(form)


class TaskList(ListView):
    model = Task

class AuthView(LoginView):
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse_lazy('cabinet')

    def form_invalid(self, form):
        return self.render_to_response(self.get_context_data(form=form))

class DeleteTaskView(DeleteView):
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

class UpadateStatusView(UpdateView):
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

def cabinet(request):
    return HttpResponse('cabinet')

def new_task(request):
    return render(request,"New_task.html")