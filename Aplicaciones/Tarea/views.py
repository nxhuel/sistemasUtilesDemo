from django.shortcuts import render, redirect, get_object_or_404
from .forms import TaskForm
from .models import Task

# Create your views here.


def home(request):
    return render(request, 'home.html')


def tasks(request):
    tasks = Task.objects.filter(
        user=request.user, dateCompleted__isnull=True)
    return render(request, 'tasks.html', {
        'tasks': tasks
    })


def createTask(request):
    if request.method == 'GET':
        return render(request, 'createTask.html', {
            'form': TaskForm
        })
    else:
        try:
            form = TaskForm(request.POST)
            newTask = form.save(commit=False)
            newTask.user = request.user
            newTask.save()
            return redirect('tasks')
        except ValueError:
            return render(request, 'createTask.html', {
                'form': TaskForm,
                'error': 'Por favor provee datos validos'
            })


def taskDetails(request, task_id):
    task = get_object_or_404(Task, pk=task_id)
    return render(request, 'taskDetails.html', {
        'task': task
    })