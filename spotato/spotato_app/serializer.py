from rest_framework import serializers

from .models import *


class SerializerClientRegister(serializers.Serializer):
    first_name = serializers.CharField(max_length=255)
    last_name = serializers.CharField(max_length=255)
    username = serializers.CharField(max_length=100)
    email = serializers.EmailField()
    password = serializers.CharField(max_length=100)
    phone = serializers.CharField(max_length=10)

    def create(self, validated_data):
        user = User.objects.create_user(
            first_name=validated_data["first_name"],
            last_name=validated_data["last_name"],
            email=validated_data["email"],
            username=validated_data["username"],
            password=validated_data["password"],
        )
        return Client.objects.create(user, phone=validated_data['phone'])


class SerializerSpotterRegister(SerializerClientRegister):
    def create(self, validated_data):
        user = User.objects.create_user(
            first_name=validated_data["first_name"],
            last_name=validated_data["last_name"],
            email=validated_data["email"],
            username=validated_data["username"],
            password=validated_data["password"],
        )
        return Spotter.objects.create(user, phone=validated_data['phone'])


class RequeteSerializer(serializers.Serializer):
    pass
