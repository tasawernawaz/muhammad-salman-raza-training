from django.urls import path

from .views import (
    SignupForm,
    GreetUser,
    LoginForm,
    LogoutUser,
    DeleteUser,
)

urlpatterns = [
    path("signup/", SignupForm.as_view(), name="signup"),
    path("greet/", GreetUser.as_view(), name="greet"),
    path("login/", LoginForm.as_view(), name="login"),
    path("logout/", LogoutUser.as_view(), name="logout"),
    path("delete/", DeleteUser.as_view(), name="delete"),
]
