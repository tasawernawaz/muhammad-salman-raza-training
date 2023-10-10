from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import Http404
from django.contrib.auth.models import User

from .forms import TaskCreationForm
from .models import Task

# Create your views here.


class HomeView(LoginRequiredMixin, View):
    template = "home.html"

    def get(self, request):
        user_profile = request.user.userprofile

        if user_profile.user.is_superuser:
            tasks = Task.objects.all()
        else:
            tasks = Task.objects.filter(user=user_profile)

        tasks = tasks.order_by("status", "due_date")
        context = {"tasks": tasks}
        return render(request, self.template, context)


class CreateTask(LoginRequiredMixin, View):
    form_class = TaskCreationForm
    template_name = "create.html"
    redirect_path = "home"
    title = "Create a task"

    def get(self, request):
        form = self.form_class()
        context = {"title": self.title, "form": form}
        return render(request, self.template_name, context)

    def post(self, request):
        form = self.form_class(request.POST)

        if form.is_valid():
            task = form.save(commit=False)
            task.user = request.user.userprofile
            task.save()
            return redirect(self.redirect_path)
        else:
            errors = form.errors

        context = {"title": self.title, "form": form, "errors": errors}
        return render(request, self.template_name, context)


class EditTaskView(LoginRequiredMixin, View):
    form_class = TaskCreationForm
    template_name = "edit.html"
    redirect_home = "home"
    redirect_login = "login"
    title = "Edit task"

    def get(self, request, task_id):
        try:
            task = Task.objects.get(id=task_id)

            if (task.user.user.username == request.user.username) or (
                request.user.userprofile.user.is_superuser
            ):
                users = User.objects.all()
                form = self.form_class(instance=task)
                context = {"title": self.title, "form": form, "users": users}
                return render(request, self.template_name, context)
            else:
                raise Http404("Task does not exist")
        except:
            raise Http404("Task does not exist")

    def post(self, request, task_id):
        task = Task.objects.get(id=task_id)
        form = self.form_class(request.POST, instance=task)

        if form.is_valid():
            print(task)
            form.save()
            return redirect(self.redirect_home)
        else:
            errors = form.errors

        context = {"title": self.title, "form": form, "errors": errors}
        return render(request, self.template_name, context)


class DeleteTask(LoginRequiredMixin, View):
    template = "home"

    def get(self, request, task_id):
        try:
            task = Task.objects.get(id=task_id)
            task.delete()
        except:
            raise Http404("Task does not exist")
        return redirect(self.template)