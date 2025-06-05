
# -----------------  DIFFERENT TYPES OF FIELDS IN DJANGO MODELS -----------------

# CharFields         short text strings like titles or names (max_length is required)
# TextFields         longer text strings, like descriptions or content (no max_length required)
# IntegerFields      whole numbers
# DateFields         dates
# DatetimeFields     date and time
# BooleanFields      True/False values
# NullBooleanFields  True/False or None values
# FloatFields        decimal numbers (3.14)
# DecimalFields      fixed-point decimal numbers (money, prices) (requires max_digits and decimal_places)
# UrlFields          URLs
# SlugFields         URL-friendly strings
# ChoicesFields      fields with a limited set of choices
# FileField          uploading files
# ImageField         uploading images
# EmailField         storing email addresses

# null=False	     The field cannot be NULL in the database (must have a value).
# null=False	     The field is required in Django forms/admin.

# class names should be capitalized and singular, e.g., Task instead of tasks

from django.db import models 
from django.contrib.auth.models import User # built-in User model
    
PRIORITY_CHOICES = [
    ('Low', 'Low'), # first element is the value stored in the database, second is the human-readable name (what user sees in forms)
    ('Normal', 'Normal'),
    ('High', 'High'),
]

class Task(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    task_name = models.CharField(max_length=100, null=False, blank=False)
    due_date = models.DateField(null=True, blank=True)
    completed = models.BooleanField(default=False, null=False, blank=False)
    description = models.CharField(max_length=1000, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    priority = models.CharField(max_length=10, choices=PRIORITY_CHOICES, default='Normal')

    class Meta:
        ordering = ['due_date', 'priority']

    def __str__(self):
        return self.task_name
