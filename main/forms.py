from django import forms
from .models import TaskModel

class TaskForm(forms.ModelForm):
    class Meta:
        model = TaskModel
        fields = '__all__'
        widgets = {
            'task': forms.TextInput(attrs={"placeholder": "Your task"}),
        }
