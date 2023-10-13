from django.urls import path

from task.api.views import (
    TaskList,
    SpecficTask,
    UpdateTask,
    DeleteTask,
)

urlpatterns = [
    path("tasks/", TaskList.as_view(), name="tasks"),
    path("tasks/<str:pk>/", SpecficTask.as_view(), name="specific-task"),
    path("tasks/update/<str:pk>/", UpdateTask.as_view(), name="task-update"),
    path("tasks/delete/<str:pk>/", DeleteTask.as_view(), name="task-delete"),
]
