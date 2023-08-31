from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from django.contrib.auth import authenticate, login

from .forms import UserRegisterationForm, UserLoginForm
from .models import UserProfile

# Create your views here.

def signup_view(request):
    form = UserRegisterationForm(request.POST or None)

    if(form.is_valid()):
        user = form.save()
        form = UserRegisterationForm()
        greet_url = reverse('greet') + f'?user_id={user.id}'
        request.session['greet_from_form'] = True
        return redirect(greet_url)
    else:
        print(form.errors)

    context = {'title': 'Sign up', 'form': form, 'errors': form.errors}
    template_name = 'signup.html'
    return render(request, template_name, context)

def login_view(request):
    form = UserLoginForm(request.POST or None)

    if form.is_valid():
        username = form.cleaned_data['username']
        password = form.cleaned_data['password']
        user = get_object_or_404(UserProfile, username=username)

        if (user) and (user.username == username):
            greet_url = reverse('greet') + f'?user_id={user.id}'
            request.session['greet_from_form'] = True
            return redirect(greet_url)
        else:
            errors = "Incorrect username or password."
    else:
        errors = form.errors

    context = {'title': 'Log in', 'form': form, 'errors': errors}
    template_name = 'login.html'
    return render(request, template_name, context)

def greet_user(request, user_id = None):
    user_id = request.GET.get('user_id')
    greet_from_form = request.session.pop('greet_from_form', False)

    if greet_from_form and user_id:
        user = UserProfile.objects.get(id=user_id)
    else:
        signup_url = reverse('signup')
        return redirect(signup_url)
    
    context = {'user': user}
    return render(request, 'greet.html', context)
