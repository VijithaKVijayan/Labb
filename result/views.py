from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets

from result.models import ResultUpload
from result.serializer import ResultUploadSerializer


class ResultUploadviewset(viewsets.ModelViewSet):
    queryset = ResultUpload.objects.all()
    serializer_class = ResultUploadSerializer