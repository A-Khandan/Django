from django.contrib import admin
from django.urls import path
from .views import homeView, task_list, task_create, task_edit, signup_view, task_status_update
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('', homeView.as_view(), name='home'),
    path('tasks/', task_list, name='task_list'),
    path('tasks/new/', task_create, name='task_create'),
    path('tasks/<int:task_id>/edit/', task_edit, name='task_edit'),
    path('tasks/<int:task_id>/statusUpdate', task_status_update, name='status_update'),
    path('signup/', signup_view, name='signup'),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='login'), name='logout')
]