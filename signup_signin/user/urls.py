from django.urls import path

from .views import (
    signup_view,
    greet_user,
    login_view,
)

urlpatterns = [
    path('signup/', signup_view, name='signup'),
    path('greet/', greet_user, name='greet'),
    path('login/', login_view, name='login'),
]
