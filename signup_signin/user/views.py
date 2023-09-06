from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

from .forms import UserRegisterationForm, UserLoginForm

# Create your views here.

def signup_view(request):
    if request.user.is_authenticated:
        return redirect('greet')
    form = UserRegisterationForm(request.POST or None)

    if form.is_valid():
        user = form.save(commit=False)
        user.set_password(form.cleaned_data['password'])
        user.save()
        login(request, user)

        return redirect('greet')

    context = {'title': 'Sign up', 'form': form, 'errors': form.errors}
    template_name = 'signup.html'
    return render(request, template_name, context)

def login_view(request):
    if request.user.is_authenticated:
        return redirect('greet')
    form = UserLoginForm(request.POST or None)

    if form.is_valid():
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('greet')
        else:
            errors = "Incorrect username or password."
    else:
        errors = form.errors

    context = {'title': 'Log in', 'form': form, 'errors': errors}
    template_name = 'login.html'
    return render(request, template_name, context)

@login_required
def logout_user(request):
    logout(request)
    return redirect('login')

@login_required
def delete_user(request):
    user = request.user
    user.delete()
    return redirect('signup')

@login_required
def greet_user(request):
    return render(request, 'greet.html')
