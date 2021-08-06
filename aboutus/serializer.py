from rest_framework import serializers

from aboutus.models import Home, Aboutus, AboutUsImage, HomeImage


class HomeSerializer(serializers.ModelSerializer):

    class Meta:
        model=Home
        fields=(
            "description",
            "contactdetail",
        )

class HomeImageSerializer(serializers.ModelSerializer):

    class Meta:
        model=HomeImage
        fields=(
            "home",
            "img",
        )

class AboutusSerializer(serializers.ModelSerializer):

    class Meta:
        model=Aboutus
        fields=(
            "description",

        )


class AboutUsImageSerializer(serializers.ModelSerializer):
    class Meta:
        model =AboutUsImage
        fields = (
            "aboutus",
            "img",

        )