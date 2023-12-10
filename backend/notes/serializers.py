from .models import Todo
from rest_framework import serializers


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todo
        exclude = ["owner"]
