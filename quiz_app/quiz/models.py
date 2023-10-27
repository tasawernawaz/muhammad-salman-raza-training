from django.contrib.auth.models import User
from django.db import models


class Quiz(models.Model):
    title = models.CharField(max_length=100, blank=False)
    permalink_id = models.CharField(max_length=6, unique=True)
    published = models.BooleanField(default=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class Question(models.Model):
    question = models.TextField(max_length=100, blank=False)
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE, related_name="questions")

    def __str__(self):
        return self.question


class Option(models.Model):
    option = models.CharField(max_length=20, blank=False)
    is_answer = models.BooleanField(default=False)
    question = models.ForeignKey(
        Question, on_delete=models.CASCADE, related_name="options"
    )

    def __str__(self):
        return self.option
