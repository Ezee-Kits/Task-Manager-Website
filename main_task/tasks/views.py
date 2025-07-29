from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Task
from .forms import TaskForm


def home(request):
    form = TaskForm()
    context={'tasks':Task.objects.all(),'form':form}
    return render(request,'tasks/home.html',context=context)

def about(request):
    return render(request,'tasks/about.html')