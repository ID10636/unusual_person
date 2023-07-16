import django.utils.timezone
from django.db import models
from django.urls import reverse_lazy

# Create your models here.

class Task(models.Model):
    title = models.CharField(max_length=50)
    body = models.TextField(blank=True, null=True)
    created_at = models.DateField(auto_now_add=True)
    deadline = models.DateField(default=django.utils.timezone.now())

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse_lazy('tasks:all_tasks')
