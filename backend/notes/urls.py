from .viewsets import TaskListCreateApiView, TaskDetailView
from django.urls import path


urlpatterns = [
    path("todos/", TaskListCreateApiView.as_view(), name="todo-list-create"),
    path("todos/<int:pk>/", TaskDetailView.as_view(), name="todo-detail"),
]
