from django.contrib.auth.models import User
from rest_framework import serializers


class UserSignupSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            "email",
            "first_name",
            "last_name",
            "password",
            "username",
        ]


class UserLoginSerializer(serializers.Serializer):
    class Meta:
        model = User
        fields = ["email", "password"]
