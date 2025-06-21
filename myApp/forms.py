from django import forms
from .models import Task
from django.utils import timezone
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['task_name', 'description', 'due_date', 'priority']
        widgets = {
            'due_date': forms.DateInput(attrs={'type': 'date'}),
        }

    def clean_due_date(self):
        due_date = self.cleaned_data.get('due_date')
        if due_date and due_date < timezone.now().date():
            raise forms.ValidationError("Due date cannot be in the past.")
        return due_date
    
    def __init__(self, *args, **kwargs):
        editing = kwargs.pop('editing', False)
        super().__init__(*args, **kwargs)
        if editing:
            self.fields['completed'] = forms.BooleanField(required=False)


class NewSignupForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        field_classes = (
            "w-full bg-transparent border border-gray-600 text-white "
            "placeholder-gray-400 rounded px-3 py-2 focus:outline-none "
            "focus:ring-2 focus:ring-blue-500"
        )
        for field in self.fields.values():
            field.widget.attrs.update({'class': field_classes})

