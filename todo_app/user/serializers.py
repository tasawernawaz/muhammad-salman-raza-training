from rest_framework import serializers
from django.contrib.auth.models import User


class UserLoginSerializer(serializers.Serializer):
    class Meta:
        model = User
        fields = ["username", "password"]


class UserSignupSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            "first_name",
            "last_name",
            "email",
            "username",
            "password",
        ]
