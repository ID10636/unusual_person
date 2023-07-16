from django.forms import ModelForm
from .models import Task
from django import forms

class TaskForm(ModelForm):
    class Meta:
        model = Task
        fields = ['title','body','deadline']
