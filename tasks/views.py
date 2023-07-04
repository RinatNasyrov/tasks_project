from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def authorization(request):
    return HttpResponse('auth')

def cabinet(request):
    return HttpResponse('cabinet')

def new_task(request):
    return HttpResponse('new task')