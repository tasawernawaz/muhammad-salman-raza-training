import uuid
from django.db import models
from django.contrib.auth.models import User


class Task(models.Model):
    task_id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    title = models.CharField(max_length=100, blank=False)
    description = models.TextField(blank=False)
    due_date = models.DateField(null=False)
    status = models.BooleanField(default=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
