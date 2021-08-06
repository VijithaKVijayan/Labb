from rest_framework import serializers

from result.models import ResultUpload
from user.serializer import UserSerializer


class ResultUploadSerializer(serializers.ModelSerializer):
    user=UserSerializer()
    class Meta:
        model=ResultUpload
        fields=(
            "id",
            "resultfile",
            "user",
        )