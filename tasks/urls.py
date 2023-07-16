from django.urls import path, include
from . import views

app_name = 'tasks'

urlpatterns = [
    path('', views.TaskListView.as_view(), name='all_tasks'),
    path('<int:pk>', views.TaskDetailView.as_view(), name='task_detail'),
    path('<int:pk>/delete', views.TaskDeleteView.as_view(), name='task_delete'),
    path('<int:pk>/update', views.TaskUpdateView.as_view(), name='task_update'),
    path('new', views.TaskCreateView.as_view(), name='new_task'),
]
