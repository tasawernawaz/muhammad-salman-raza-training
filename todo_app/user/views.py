from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import UserProfile

from .forms import UserRegisterationForm, UserLoginForm


class SignupForm(View):
    form_class = UserRegisterationForm
    template_name = "signup.html"
    redirect_tasks = "tasks"
    title = "Sign up"

    def get(self, request):
        if request.user.is_authenticated:
            return redirect(self.redirect_tasks)
        form = self.form_class()
        context = {"title": self.title, "form": form}
        return render(request, self.template_name, context)

    def post(self, request):
        form = self.form_class(request.POST)

        if form.is_valid():
            user = form.save()
            profile = UserProfile(user=user)
            profile.save()
            login(request, user)
            return redirect(self.redirect_tasks)
        else:
            errors = form.errors

        context = {"title": self.title, "form": form, "errors": errors}
        return render(request, self.template_name, context)


class LoginForm(View):
    form_class = UserLoginForm
    template_name = "login.html"
    redirect_name = "home"
    redirect_tasks = "tasks"
    title = "Log in"

    def get(self, request):
        if request.user.is_authenticated:
            return redirect(self.redirect_tasks)
        form = self.form_class()
        context = {"title": self.title, "form": form}
        return render(request, self.template_name, context)

    def post(self, request):
        form = self.form_class(request.POST)

        if form.is_valid():
            username = request.POST["username"]
            password = request.POST["password"]

            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect(self.redirect_tasks)
            else:
                errors = "Incorrect username or password."
        else:
            errors = form.errors

        context = {"title": self.title, "form": form, "errors": errors}
        return render(request, self.template_name, context)


class LogoutUser(LoginRequiredMixin, View):
    template = "login"

    def get(self, request):
        logout(request)
        return redirect(self.template)


class DeleteUser(LoginRequiredMixin, View):
    template = "signup"

    def get(self, request):
        user = request.user
        user.delete()
        return redirect(self.template)
