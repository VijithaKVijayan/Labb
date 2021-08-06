from django.contrib.auth import models
from django.db.models.base import Model
from rest_framework import serializers
from django.contrib.auth.models import User




class UserCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields=(
            "username",
            "password",
            "email",
        )
   # def create(self,validated_data):
    #    return User.objects.create_user(username=validated_data['username'],password=validated_data['password'],email=validated_data['email'])

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields=(
                "username",
                "email"
            )