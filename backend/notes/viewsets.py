from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from .models import Todo
from .serializers import TaskSerializer


class TaskListCreateApiView(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    # queryset = Todo.objects.all()
    serializer_class = TaskSerializer

    def get_queryset(self):
        user = self.request.user
        return Todo.objects.filter(owner=user)

    def perform_create(self, serializer):
        # Set the owner before saving the instance
        serializer.save(owner=self.request.user)


class TaskDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = TaskSerializer
    # queryset = Todo.objects.all()

    def get_queryset(self):
        user = self.request.user
        return Todo.objects.filter(owner=user)
