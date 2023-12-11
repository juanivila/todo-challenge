from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics
from rest_framework.filters import SearchFilter
from rest_framework.permissions import IsAuthenticated

from .models import Todo
from .serializers import TaskSerializer


class TaskListCreateApiView(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = TaskSerializer

    # Add filtering and search by title and description
    filter_backends = [DjangoFilterBackend, SearchFilter]
    filterset_fields = ["completed", "due_date"]
    search_fields = ["title", "description"]

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
