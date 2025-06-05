from django.contrib import admin
from .models import Task
# We use admin.py to register the models so they appear in the Django Admin interface

@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('task_name', 'priority', 'completed', 'due_date')
    list_filter = ('priority', 'completed')
    search_fields = ('task_name', 'description')