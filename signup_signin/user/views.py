from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin

from .forms import UserRegisterationForm, UserLoginForm

# Create your views here.


class SignupForm(View):
    form_class = UserRegisterationForm
    template_name = "signup.html"
    redirect_name = "greet"
    title = "Sign up"

    def get(self, request):
        if request.user.is_authenticated:
            return redirect(self.redirect_name)
        form = self.form_class()
        context = {"title": self.title, "form": form}
        return render(request, self.template_name, context)

    def post(self, request):
        form = self.form_class(request.POST)

        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data["password"])
            user.save()
            login(request, user)

            return redirect(self.redirect_name)
        else:
            errors = form.errors

        context = {"title": self.title, "form": form, "errors": errors}
        return render(request, self.template_name, context)


class LoginForm(View):
    form_class = UserLoginForm
    template_name = "login.html"
    redirect_name = "greet"
    title = "Log in"

    def get(self, request):
        if request.user.is_authenticated:
            return redirect(self.redirect_name)
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
                return redirect(self.redirect_name)
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


class GreetUser(LoginRequiredMixin, View):
    template = "greet.html"

    def get(self, request):
        return render(request, self.template)
