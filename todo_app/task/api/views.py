from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated

from task.models import Task
from task.serializers import TaskSerializer


class TaskList(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user_profile = request.user

        if user_profile.is_superuser:
            tasks = Task.objects.all()
        else:
            tasks = Task.objects.filter(user=user_profile)

        tasks = tasks.order_by("status", "due_date")
        serializer = TaskSerializer(tasks, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = TaskSerializer(data=request.data)
        if serializer.is_valid():
            if not request.user.is_superuser:
                serializer.save(user=request.user)
            else:
                serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class SpecficTask(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, pk):
        try:
            task = Task.objects.get(task_id=pk)
            if (task.user.username == request.user.username) or (
                request.user.is_superuser
            ):
                serializer = TaskSerializer(task, many=False)
                return Response(serializer.data)
            return Response(status=status.HTTP_403_FORBIDDEN)
        except Task.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)


class UpdateTask(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, pk):
        try:
            task = Task.objects.get(task_id=pk)
            if (task.user.username == request.user.username) or (
                request.user.is_superuser
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
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        except Task.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)


class DeleteTask(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, pk):
        try:
            task = Task.objects.get(task_id=pk)
            if (task.user.username == request.user.username) or (
                request.user.is_superuser
            ):
                serializer = TaskSerializer(task, many=False)
                return Response(serializer.data)
            return Response(status=status.HTTP_403_FORBIDDEN)
        except Task.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def delete(self, request, pk):
        try:
            task = Task.objects.get(task_id=pk)
            if (task.user.username == request.user.username) or (
                request.user.is_superuser
            ):
                task.delete()
                return Response(status=status.HTTP_200_OK)
            return Response(status=status.HTTP_403_FORBIDDEN)
        except Task.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
