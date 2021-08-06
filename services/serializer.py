from django.contrib.auth import models
from django.db.models.base import Model
from rest_framework import serializers
from .models import Service, SubService, SubTime
from user.serializer import UserSerializer

class ServiceSerializer(serializers.ModelSerializer):
    user=UserSerializer()
    class Meta:
        model=Service
        fields=(
            "id",
            "user",
            "name",
        )

class SubServiceSerializer(serializers.ModelSerializer):
    service=ServiceSerializer()
    class Meta:
        model=SubService
        fields=(
            "id",
            "service",
            "name",
        )

class SubTimeSerializer(serializers.ModelSerializer):
    servicename=ServiceSerializer()
    subservice=SubServiceSerializer()
    class Meta:
        model=SubTime
        fields=(
            "id",
            "servicename",
            "subservice",
            "TimeSlot",
            "Date",
        )

