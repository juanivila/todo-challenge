import logging
from datetime import datetime, timezone

from django.contrib.auth.models import User
from rest_framework import serializers

from .models import Todo

logger = logging.getLogger("django")


class TaskSerializer(serializers.ModelSerializer):
    title = serializers.CharField(min_length=5)
    description = serializers.CharField(max_length=200)

    class Meta:
        model = Todo
        fields = ["id", "title", "description", "completed", "due_date"]

    def validate_owner(self, value):
        """
        Checks if the specified owner user exists in the database.
        """

        if not User.objects.filter(id=value.id).exists():
            raise serializers.ValidationError("Invalid owner specified.")
        return value

    def validate(self, data):
        """
        Checks if the due_date is before the current date
        """
        due_date = data.get("due_date")

        # Create a timezone-aware datetime object for the current date
        current_date = datetime.now(timezone.utc).replace(
            hour=0, minute=0, second=0, microsecond=0
        )

        if due_date and due_date < current_date:
            error_message = "Due date cannot be in the past."
            logger.info("Validating data", extra={"request": self.context["request"]})
            raise serializers.ValidationError(error_message)
        return data
