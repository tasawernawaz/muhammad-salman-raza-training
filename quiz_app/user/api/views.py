from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.hashers import make_password
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from user.serializers import UserLoginSerializer, UserSignupSerializer

from .permissions import SignupSigninPermission


class SignupApi(APIView):
    permission_classes = [SignupSigninPermission]

    def post(self, request):
        serializer = UserSignupSerializer(data=request.data)

        if serializer.is_valid():
            password = serializer.validated_data["password"]
            hashed_password = make_password(password)
            serializer.validated_data["password"] = hashed_password

            user = serializer.save()
            login(request, user)

            return Response(status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class LoginApi(APIView):
    permission_classes = [SignupSigninPermission]

    def post(self, request):
        serializer = UserLoginSerializer(data=request.data)
        if serializer.is_valid():
            try:
                username = request.data["username"]
                password = request.data["password"]
            except:
                return Response(status=status.HTTP_400_BAD_REQUEST)

            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return Response(status=status.HTTP_200_OK)
            else:
                error = {"credentials": "Incorrect username or password."}
                return Response(error, status=status.HTTP_400_BAD_REQUEST)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class LogoutApi(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        logout(request)
        return Response(status=status.HTTP_200_OK)


class DeleteUserApi(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        user = request.user
        user.delete()
        return Response(status=status.HTTP_200_OK)
