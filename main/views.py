from django.shortcuts import render , redirect
from .models import TaskModel
from .forms import TaskForm
# Create your views here.

def index(request):
    tasks = TaskModel.objects.all()

    form = TaskForm()
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/")

    context = {'form':form , 'tasks':tasks}
    return render(request , 'main/index.html' , context)

def update_task(request , pk):
    task = TaskModel.objects.get(id=pk)

    form = TaskForm(instance=task)
    if request.method == 'POST':
        form = TaskForm(request.POST , instance=task)
        if form.is_valid():
            form.save()
        return redirect("/")
    context = {'task':task , 'form':form}
    return render(request , 'main/update_task.html' , context)


def delete_task(request , pk):
    task = TaskModel.objects.get(id=pk)
    task.delete()
    return redirect("/")