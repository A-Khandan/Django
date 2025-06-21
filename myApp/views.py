
# A view in Django is a Python function (or class) that:
#  Takes a request from the browser
#  Processes data (e.g. fetches tasks from the database)
#  Returns a response, usually by rendering an HTML template

from .models import Task
from .forms import TaskForm, NewSignupForm

from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from django.views.decorators.http import require_POST
from django.http import HttpResponse, JsonResponse

from django.contrib.auth import login 
from django.contrib import messages
from django.contrib.auth.decorators import login_required

class homeView(View):
    def get(self, request): # 'request' is an instance of HttpRequest class, it represents everything the brower sent to the server
        return render(request, 'home.html')
    
def signup_view(request):
    if request.method == 'POST':
        form = NewSignupForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('task_list')
    else:
        form = NewSignupForm()
    return render(request, 'signup.html', {'form': form})
    
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
            messages.success(request, "Task updated!")
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
            task.user = request.user  
            task.save()
            messages.success(request, "Yay! you added a new task.")
            return redirect('task_list')
    else:
        form = TaskForm()
    return render(request, 'task_form.html', {'form': form})

@require_POST
@login_required
def task_status_update(request, task_id):
    task = get_object_or_404(Task, id= task_id, user=request.user)
    task.completed = not task.completed
    task.save()
    return JsonResponse({'completed': task.completed})
