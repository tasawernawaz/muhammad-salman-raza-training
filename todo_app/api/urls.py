from django.urls import path

from .views import (
    UpdateTaskStatus,
)

urlpatterns = [
    path(
        "update-task-status/<int:task_id>/",
        UpdateTaskStatus.as_view(),
        name="update_task_status",
    ),
]
