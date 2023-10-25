from django.urls import path

from .api.views import (
    SignupApi,
    LoginApi,
    LogoutApi,
    DeleteUserApi,
)

urlpatterns = [
    path("signup/", SignupApi.as_view(), name="signup"),
    path("login/", LoginApi.as_view(), name="login"),
    path("logout/", LogoutApi.as_view(), name="logout"),
    path("delete/", DeleteUserApi.as_view(), name="delete"),
]
