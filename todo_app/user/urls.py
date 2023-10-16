from django.urls import path

from .views import (
    SignupForm,
    LoginForm,
    LogoutUser,
    DeleteUser,
)

urlpatterns = [
    path("signup/", SignupForm.as_view(), name="signup"),
    path("login/", LoginForm.as_view(), name="login"),
    path("logout/", LogoutUser.as_view(), name="logout"),
    path("delete/", DeleteUser.as_view(), name="delete"),
]
