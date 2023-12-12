import logging

from django.db import IntegrityError
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics, serializers, status
from rest_framework.filters import SearchFilter
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from .models import Todo
from .serializers import TaskSerializer

logger = logging.getLogger("django")


class TaskListCreateApiView(generics.ListCreateAPIView):
    """
    List and create tasks.

    Allows authenticated users to list and create tasks.
    """

    serializer_class = TaskSerializer
    permission_classes = [IsAuthenticated]

    # Add filtering and search by title and description
    filter_backends = [DjangoFilterBackend, SearchFilter]
    filterset_fields = ["completed", "due_date"]
    search_fields = ["title", "description"]

    def get_queryset(self):
        """
        Get the queryset of Todo tasks for this view.

        Parameters: None

        Functionality:
        - Gets the current authenticated user from the request.
        - Filters the Todo queryset to only return tasks belonging to the current user.
        - Returns the filtered queryset.

        """

        current_user = self.request.user
        return Todo.objects.filter(owner=current_user)

    def perform_create(self, serializer):
        """
        Custom perform_create method to handle task creation.

        Parameters:
        - serializer: The serializer containing the data to create.

        Functionality:
        - Saves the task, setting the owner to the requesting user.
        - Logs successful creation.
        - Returns 201 response with serialized data.

        - Catches IntegrityError, logs error, and returns 500 validation error.

        - Catches any other Exceptions, logs error, and returns 500 validation error.

        """
        try:
            serializer.save(owner=self.request.user)
            logger.info("Task was created")
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        except IntegrityError:
            msg = "An integrity error occurred during task creation."
            logger.error(msg)
            response_data = {"error": msg}
            raise serializers.ValidationError(
                response_data, code=status.HTTP_500_INTERNAL_SERVER_ERROR
            )

        except Exception as e:
            msg = f"An unexpected error occurred during task creation: {e}"
            logger.error(msg)
            response_data = {"error": msg}

            raise serializers.ValidationError(
                response_data, code=status.HTTP_500_INTERNAL_SERVER_ERROR
            )


class TaskDetailView(generics.RetrieveUpdateDestroyAPIView):
    """
    Get, update, or delete a specific task.

    Only the owner of the task can perform these actions.
    """

    serializer_class = TaskSerializer

    def get_queryset(self):
        """
        Get the queryset of Todo tasks for this view.

        Parameters: None

        Functionality:
        - Gets the current authenticated user from the request.
        - Filters the Todo queryset to only return the task belonging to the current user.
        - Returns the filtered queryset.

        """

        current_user = self.request.user
        return Todo.objects.filter(owner=current_user)
