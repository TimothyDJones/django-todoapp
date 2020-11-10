from django.shortcuts import render, HttpResponse, redirect
from .forms import TaskForm
from .models import Task

# Create your views here.

def index(request):
    #return HttpResponse("Hello, World!")
    form = TaskForm()

    if request.method == 'POST':
        # get the posted form data
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("index")
    
    tasks = Task.objects.all()

    return render(request, "index.html", {"task_form": form, "tasks": tasks})
