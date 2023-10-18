from rest_framework import permissions
from task.models import Task

class TaskAccessPermission(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.user.is_superuser:
            return True

        task_id = view.kwargs.get('pk')
        task = Task.objects.get(task_id=task_id)
        return task.user == request.user
