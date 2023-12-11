import logging

from django.db import IntegrityError
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics, serializers, status
from rest_framework.filters import SearchFilter
from rest_framework.permissions import IsAuthenticated

from .models import Todo
from .serializers import TaskSerializer


logger = logging.getLogger("django")


class TaskListCreateApiView(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = TaskSerializer

    # Add filtering and search by title and description
    filter_backends = [DjangoFilterBackend, SearchFilter]
    filterset_fields = ["completed", "due_date"]
    search_fields = ["title", "description"]

    def get_queryset(self):
        logger.info("Filtering task by current user")
        user = self.request.user
        return Todo.objects.filter(owner=user)

    def perform_create(self, serializer):
        # Set the owner before saving the instance

        try:
            serializer.save(owner=self.request.user)
            logger.info("Task was created")

        except IntegrityError as e:
            logger.error(f"IntegrityError during task creation: {e}")
            response_data = {"error": "Task creation failed due to integrity error."}
            raise serializers.ValidationError(
                response_data, code=status.HTTP_400_BAD_REQUEST
            )

        except Exception as e:
            logger.error(f"An unexpected error occurred during task creation: {e}")
            response_data = {
                "error": "An unexpected error occurred during task creation."
            }
            raise serializers.ValidationError(
                response_data, code=status.HTTP_500_INTERNAL_SERVER_ERROR
            )


class TaskDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = TaskSerializer
    # queryset = Todo.objects.all()

    def get_queryset(self):
        user = self.request.user
        return Todo.objects.filter(owner=user)
