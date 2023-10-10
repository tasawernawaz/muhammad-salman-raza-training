from django.urls import path

from .views import (
    CreateTask,
    HomeView,
    EditTaskView,
    DeleteTask,
)

urlpatterns = [
    path("create/", CreateTask.as_view(), name="create-task"),
    path("home/", HomeView.as_view(), name="home"),
    path("edit/<int:task_id>/", EditTaskView.as_view(), name="edit-task"),
    path("delete-task/<int:task_id>/", DeleteTask.as_view(), name="delete-task"),
]
