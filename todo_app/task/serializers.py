from rest_framework import serializers
from .models import Task


class TaskSerializer(serializers.ModelSerializer):
    task_uuid = serializers.ReadOnlyField(source="task_id")

    class Meta:
        model = Task
        fields = ["title", "description", "due_date", "status", "task_uuid"]
