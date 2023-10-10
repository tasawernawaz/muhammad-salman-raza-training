from django import forms
from django.utils import timezone

from .models import Task


class TaskCreationForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ["title", "description", "due_date", "user"]

    def clean_due_date(self):
        due_date = self.cleaned_data.get("due_date")
        if due_date and due_date <= timezone.now().date():
            raise forms.ValidationError("Due date must be in the future.")
        return due_date
