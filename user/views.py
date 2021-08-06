from django.shortcuts import render

# Create your views here.
# local
from .serializer import UserCreateSerializer
from django.contrib.auth.models import User

# restframework
from rest_framework import viewsets


class userviewset(viewsets.ModelViewSet):
    queryset=User.objects.all()
    serializer_class= UserCreateSerializer