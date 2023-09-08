from django.urls import path

from .views import (
    # signup_view,
    SignupForm,
    # greet_user,
    GreetUser,
    # login_view,
    LoginForm,
    # logout_user,
    LogoutUser,
    # delete_user,
    DeleteUser,
)

urlpatterns = [
    path('signup/', SignupForm.as_view(), name='signup'),
    path('greet/', GreetUser.as_view(), name='greet'),
    path('login/', LoginForm.as_view(), name='login'),
    path('logout/', LogoutUser.as_view(), name='logout'),
    path('delete/', DeleteUser.as_view(), name='delete'),
]
