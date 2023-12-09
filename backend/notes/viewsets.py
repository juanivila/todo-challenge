from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from .models import Todo
from .serializers import TaskSerializer


class TaskListCreateApiView(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Todo.objects.all()
    serializer_class = TaskSerializer


class TaskDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Todo.objects.all()
    serializer_class = TaskSerializer
