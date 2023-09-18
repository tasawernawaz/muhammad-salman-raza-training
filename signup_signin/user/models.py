from django.contrib.auth.models import AbstractUser
from django.db import models
from .validators import validate_date_of_birth

# Create your models here.


class UserProfileQuerySet(models.QuerySet):
    def admins(self):
        return self.filter(is_superuser=True)

    def users(self):
        return self.filter(is_superuser=False)


class UserProfileManager(models.Manager):
    def get_queryset(self):
        return UserProfileQuerySet(self.model, using=self._db)

    def admins(self):
        return self.get_queryset().admins()

    def users(self):
        return self.get_queryset().users()

    def get_by_natural_key(self, username):
        return self.get(username=username)


class UserProfile(AbstractUser):
    city = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    date_of_birth = models.DateField(null=True, validators=[validate_date_of_birth])
    full_name = models.CharField(max_length=100, default="")

    objects = UserProfileManager()
