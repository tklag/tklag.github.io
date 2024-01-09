from django.shortcuts import render
from django.http import HttpResponse

from .models import Task
# Create your views here.

def index(request):
    return render(request, "tasks/index.html",{
        "tasks": Task.objects.all()
    })

def task(request):
    if request.method == "post":
        name = name,
        details = details,
        duration = duration
    else:
        return render(request, "tasks/task.html",{
            "tasks": Task.objects.all()
        })