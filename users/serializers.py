from rest_framework import serializers
from django.contrib.auth.models import User
from .models import AdminProfile
from rest_framework.authtoken.models import Token

class AdminUserSerializer(serializers.ModelSerializer):
    """Handles admin user signup"""
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'password']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        AdminProfile.objects.create(user=user) 
        token, created = Token.objects.get_or_create(user=user) 
        return user
