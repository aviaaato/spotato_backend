from rest_framework import serializers

from .models import *


class SerializerClientRegister(serializers.Serializer):
    username = serializers.CharField(max_length=100)
    password = serializers.CharField(max_length=100)
    phone = serializers.CharField(max_length=10)

    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data["username"],
            password=validated_data["password"],
        )
        return Client.objects.create(user, phone=validated_data['phone'])


class SerializerSpotterRegister(SerializerClientRegister):
    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data["username"],
            password=validated_data["password"],
        )
        return Spotter.objects.create(user, phone=validated_data['phone'])


class RequeteSerializer(serializers.Serializer):
    pass
