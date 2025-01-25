from django.shortcuts import render, redirect,get_object_or_404
from .models import Task


def home(request):
    return render(request,'index.html')

def task_list(request):
    tasks = Task.objects.all()
    ctx = {'tasks':tasks}
    return render(request, 'tasks/task-list.html', ctx)

def create_task(request):
    if request.method == 'POST':
        title=request.POST.get('title')
        due_date=request.POST.get('due_date')
        description=request.POST.get('description')
        if title and due_date and description:
            Task.objects.create(
                title = title,
                due_date = due_date,
                description = description
            )
            return redirect('tasks:list')
    return render(request, 'tasks/task-create.html')

def task_detail(request, task_id):
    tasks = get_object_or_404(Task, pk=task_id)
    ctx = {'tasks':tasks}
    return render(request, 'tasks/task-detail.html', ctx)

def task_update(request, task_id):
    tasks = get_object_or_404(Task, pk=task_id)
    if request.method == 'POST':
        title=request.POST.get('title')
        due_date=request.POST.get('due_date')
        description=request.POST.get('description')
        if title and due_date and description:
            tasks.title = title
            tasks.due_date = due_date
            tasks.description = description
            tasks.save()
            return redirect(tasks.get_detail_url())
    ctx = {'tasks':tasks}
    return render(request, 'tasks/task-create.html', ctx)

def task_delete(request, task_id):
    tasks = get_object_or_404(Task, pk=task_id)
    tasks.delete()
    return redirect('tasks:list')