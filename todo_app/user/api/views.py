from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from user.serializers import UserLoginSerializer, UserSignupSerializer
    
class SignupApi(APIView):
    def post(self, request):
        if request.user.is_authenticated:
            error = {'Authentication status': 'Already logged in'}
            return Response(error, status=status.HTTP_400_BAD_REQUEST)

        serializer = UserSignupSerializer(data=request.data)

        if serializer.is_valid():
            user = serializer.save()
            login(request, user)

            return Response(status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class LoginApi(APIView):
    def post(self, request):
        if request.user.is_authenticated:
            error = {'Authentication status': 'Already logged in'}
            return Response(error, status=status.HTTP_400_BAD_REQUEST)
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
                error = {'credentials': 'Incorrect username or password.'}
                return Response(error, status=status.HTTP_400_BAD_REQUEST)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class LogoutApi(APIView):
    def post(self, request):
        if not request.user.is_authenticated:
            error = {'Authentication status': 'Already logged out'}
            return Response(error, status=status.HTTP_400_BAD_REQUEST)
        logout(request)
        return Response(status=status.HTTP_200_OK)
    

class DeleteUserApi(APIView):
    def post(self, request):
        if not request.user.is_authenticated:
            error = {'Authentication status': 'User must be logged in to delete their account'}
            return Response(error, status=status.HTTP_400_BAD_REQUEST)
        user = request.user
        user.delete()
        return Response(status=status.HTTP_200_OK)