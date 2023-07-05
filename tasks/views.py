from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import CreateView, ListView

from tasks.models import Task


class TaskCreate(CreateView):
    model = Task
    fields = ["description", "current_status"]

class TaskList(ListView):
    model = Task

# Create your views here.
def auth(request):
    return render(request,"Auth.html")

def cabinet(request):
    return HttpResponse('cabinet')

def new_task(request):
    return render(request,"New_task.html")