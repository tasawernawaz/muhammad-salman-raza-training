from django.urls import path

from .views import (
    CreateTask,
    HomeView,
    EditTaskView,
    DeleteTask,
    UpdateTaskStatus,
)

urlpatterns = [
    path("create/", CreateTask.as_view(), name="create-task"),
    path("home/", HomeView.as_view(), name="home"),
    path("edit/<int:task_id>/", EditTaskView.as_view(), name="edit-task"),
    path("delete-task/<int:task_id>/", DeleteTask.as_view(), name="delete-task"),
    path("update-task-status/<int:task_id>/", UpdateTaskStatus.as_view(), name="update_task_status"),
]
