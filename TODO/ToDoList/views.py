from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import *
from .forms import *

# Create your views here.
def todo(request):
    tasks = Task.objects.all()
    form = TaskForm()
    if(request.method=="POST"):
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/')
    context = {
        'tasks':tasks,
        'form':form
    }
    return render(request,'index.html',context)

    
def updateTask(request,primary_key):
    task = Task.objects.get(id=primary_key)
    form = TaskForm(instance=task)
    if(request.method=="POST"):
        form = TaskForm(request.POST,instance=task)
        if form.is_valid():
            form.save()
            return redirect('/')
    context={
        'form':form
    }
    return render(request,'update.html',context)

def deleteTask(request,primary_key):
    item = Task.objects.get(id=primary_key)
    if(request.method=="POST"):
        item.delete()
        return redirect('/')
    context={
        'item':item
    }
    return render(request,'confirm.html',context)