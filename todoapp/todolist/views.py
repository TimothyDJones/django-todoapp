from django.shortcuts import render, HttpResponse, redirect
from .forms import TaskForm

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

    return render(request, "index.html", {"task_form": form})
