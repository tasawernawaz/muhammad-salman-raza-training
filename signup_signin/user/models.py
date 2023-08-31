from django.db import models
import uuid

# Create your models here.

class UserProfile(models.Model):
    city = models.CharField(max_length=100)
    country  = models.CharField(max_length=100)
    date_of_birth = models.DateField()
    full_name = models.CharField(max_length=24)
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    username = models.SlugField(max_length=24, unique=True)
