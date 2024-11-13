from django.urls import path
from . import api_views

urlpatterns = [
    path('tasks/', api_views.TaskList.as_view(), name='task-list'),  # Example API endpoint
    path('tasks/<int:pk>/', api_views.TaskDetail.as_view(), name='task-detail'),
]
