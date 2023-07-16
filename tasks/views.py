from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import generic
from .forms import TaskForm
from .models import Task


# Create your views here.
# CRUD => CREATE READ UPDATE DELETE
class TaskListView(generic.ListView):
    model = Task
    template_name = 'tasks/all_tasks.html'
    context_object_name = 'tasks'


class TaskDetailView(generic.DetailView):
    model = Task
    template_name = 'tasks/task_detail.html'
    context_object_name = 'task'


class TaskDeleteView(generic.DeleteView):
    model = Task
    success_url = reverse_lazy('tasks:all_tasks')
    template_name = 'tasks/task_delete.html'


class TaskCreateView(generic.CreateView):
    model = Task
    form_class = TaskForm
    template_name = 'tasks/new_task.html'


class TaskUpdateView(generic.UpdateView):
    model = Task
    form_class = TaskForm
    template_name = 'tasks/task_update.html'
