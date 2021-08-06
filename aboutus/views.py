from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets

from aboutus.models import Home, HomeImage, Aboutus, AboutUsImage
from aboutus.serializer import HomeSerializer, HomeImageSerializer, AboutusSerializer, AboutUsImageSerializer


class Homeviewset(viewsets.ModelViewSet):
    queryset = Home.objects.all()
    serializer_class = HomeSerializer

class HomeImageviewset(viewsets.ModelViewSet):
    queryset = HomeImage.objects.all()
    serializer_class = HomeImageSerializer
class Aboutusviewset(viewsets.ModelViewSet):
    queryset = Aboutus.objects.all()
    serializer_class = AboutusSerializer

class AboutUsImageviewset(viewsets.ModelViewSet):
    queryset = AboutUsImage.objects.all()
    serializer_class = AboutUsImageSerializer