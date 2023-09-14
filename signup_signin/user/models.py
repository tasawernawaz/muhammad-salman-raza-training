from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.


class UserProfile(AbstractUser):
    city = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    date_of_birth = models.DateField(null=True)
    full_name = models.CharField(max_length=100, default="")
