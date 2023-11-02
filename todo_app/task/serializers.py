from rest_framework import serializers

from .models import Task


class TaskAdminSerializer(serializers.ModelSerializer):
    task_uuid = serializers.ReadOnlyField(source="task_id")

    class Meta:
        model = Task
        fields = ["title", "description", "due_date", "status", "task_uuid", "user"]


class TaskUserSerializer(serializers.ModelSerializer):
    task_uuid = serializers.ReadOnlyField(source="task_id")

    class Meta:
        model = Task
        fields = ["title", "description", "due_date", "status", "task_uuid"]


class TaskSerializer:
    def get_serializer(user):
        if user and user.is_superuser:
            return TaskAdminSerializer
        else:
            return TaskUserSerializer
