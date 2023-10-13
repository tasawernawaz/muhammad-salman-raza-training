from django.contrib.auth.mixins import LoginRequiredMixin

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from task.models import Task
from task.serializers import TaskSerializer

class TaskList(LoginRequiredMixin, APIView):
    def get(self, request):
        user_profile = request.user.userprofile
        
        if user_profile.user.is_superuser:
            tasks = Task.objects.all()
        else:
            tasks = Task.objects.filter(user=user_profile)

        tasks = tasks.order_by("status", "due_date")
        serializer = TaskSerializer(tasks, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = TaskSerializer(data=request.data)
        if serializer.is_valid():
            if not request.user.userprofile.user.is_superuser:
                serializer.save(user=request.user.userprofile)
            else:
                serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

class SpecficTask(LoginRequiredMixin, APIView):
    def get(self, request, pk):
        try:
            task = Task.objects.get(task_id=pk)
            if (task.user.user.username == request.user.username) or (
                request.user.userprofile.user.is_superuser
            ):
                serializer = TaskSerializer(task, many=False)
                return Response(serializer.data)
            return Response(status=status.HTTP_403_FORBIDDEN)
        except Task.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        
class UpdateTask(LoginRequiredMixin, APIView):
    def get(self, request, pk):
        try:
            task = Task.objects.get(task_id=pk)
            if (task.user.user.username == request.user.username) or (
                request.user.userprofile.user.is_superuser
            ):
                serializer = TaskSerializer(task, many=False)
                return Response(serializer.data)
            return Response(status=status.HTTP_403_FORBIDDEN)
        except Task.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def post(self, request, pk):
        try:
            task = Task.objects.get(task_id=pk)
            serializer = TaskSerializer(instance=task, data=request.data)
            if serializer.is_valid():
                serializer.save()
            return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
        except Task.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        

class DeleteTask(LoginRequiredMixin, APIView):
    def get(self, request, pk):
        try:
            task = Task.objects.get(task_id=pk)
            if (task.user.user.username == request.user.username) or (
                request.user.userprofile.user.is_superuser
            ):
                serializer = TaskSerializer(task, many=False)
                return Response(serializer.data)
            return Response(status=status.HTTP_403_FORBIDDEN)
        except Task.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def delete(self, request, pk):
        try:
            task = Task.objects.get(task_id=pk)
            if (task.user.user.username == request.user.username) or (
                request.user.userprofile.user.is_superuser
            ):
                task.delete()
                return Response(status=status.HTTP_200_OK)
            return Response(status=status.HTTP_403_FORBIDDEN)
        except Task.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)