
from .models import Service, SubService, SubTime
from .serializer import ServiceSerializer, SubServiceSerializer, SubTimeSerializer
# restframework
from rest_framework import viewsets


class Serviceviewset(viewsets.ModelViewSet):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer

class SubServiceviewset(viewsets.ModelViewSet):
    queryset = SubService.objects.all()
    serializer_class = SubServiceSerializer

class SubTimeviewset(viewsets.ModelViewSet):
    queryset = SubTime.objects.all()
    serializer_class = SubTimeSerializer
from django.shortcuts import render

# Create your views here.
