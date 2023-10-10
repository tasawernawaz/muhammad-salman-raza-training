from django.shortcuts import render
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import JsonResponse

from task.models import Task

# Create your views here.


class UpdateTaskStatus(LoginRequiredMixin, View):
    def post(self, request, task_id):
        try:
            task = Task.objects.get(id=task_id)
            task.status = not task.status
            task.save()
            return JsonResponse({"message": "Task status updated successfully."})
        except Task.DoesNotExist:
            return JsonResponse({"error": "Task not found."}, status=404)
