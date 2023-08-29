from rest_framework import serializers
from django.contrib.auth.models import User

from .models import UserProfile

class TokenSerializer(serializers.Serializer):
    """
        This serializer serializes the token data
    """
    access_token = serializers.CharField(max_length=255)
    refresh_token = serializers.CharField(max_length=255)


class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = "__all__"

class UserSerializer(serializers.ModelSerializer):
    # profile = UserProfileSerializer()

    class Meta:
        model = User
        fields = "__all__"



class LoginSerializer(serializers.ModelSerializer):
    # profile = UserProfileSerializer(source='userprofile', read_only=True)

    class Meta:
        model = User
        fields = ("username", "password")

# class UserSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = User
#         fields = ("username", "email")
#
#
#
# class LoginSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = User
#         fields = ("username", "password")
#
#
