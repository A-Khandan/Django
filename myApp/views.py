
# A view in Django is a Python function (or class) that:
#  Takes a request from the browser
#  Processes data (e.g. fetches tasks from the database)
#  Returns a response, usually by rendering an HTML template


from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .models import Task
from .forms import TaskForm

class homeView(View):
    def get(self, request): # 'request' is an instance of HttpRequest class, it represents everything the brower sent to the server
        return render(request, 'home.html')
    
@login_required
def task_list(request):
    tasks = Task.objects.filter(user=request.user)
    return render(request, 'task_list.html', {'tasks': tasks}) # {'tasks': tasks} = Passes the task list to a template

@login_required
def task_edit(request, task_id):
    task = get_object_or_404(Task, id=task_id, user=request.user)
    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task, editing=True)
        if form.is_valid():
            form.save()
            return redirect('task_list')
    else:
        form = TaskForm(instance=task)
    return render(request, 'task_form.html', {'form': form})

@login_required
def task_create(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.user = request.user  # link task to logged-in user
            task.save()
            return redirect('task_list')
    else:
        form = TaskForm()
    return render(request, 'task_form.html', {'form': form})