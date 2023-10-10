import uuid
from django.db import models
from user.models import UserProfile


# Create your models here.
class Task(models.Model):
    # id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=100, blank=False)
    description = models.TextField(blank=True)
    due_date = models.DateField(blank=False)
    status = models.BooleanField(default=False)
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
