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
        return Client.objects.create(user=user, phone=validated_data['phone'])


class SerializerSpotterRegister(SerializerClientRegister):
    def create(self, validated_data):
        user = User.objects.create_user(
            first_name=validated_data["first_name"],
            last_name=validated_data["last_name"],
            email=validated_data["email"],
            username=validated_data["username"],
            password=validated_data["password"],
        )
        return Spotter.objects.create(user=user, phone=validated_data['phone'])


class SerializerInputRequete(serializers.Serializer):
    label = serializers.CharField(max_length=100)
    description = serializers.CharField(max_length=255)
    categorie = serializers.IntegerField()
    latitude = serializers.CharField(max_length=100)
    longitude = serializers.CharField(max_length=100)
    duration = serializers.CharField()
    requested_start_time = serializers.DateTimeField()
    montant = serializers.FloatField()


class SerializerCategorie(serializers.ModelSerializer):
    class Meta:
        model = Categorie
        fields = ["icon", "label", "id"]


class SerializerTransaction(serializers.Serializer):
    montant = serializers.FloatField()
    source = serializers.IntegerField()
    destination = serializers.IntegerField()


# class SerializerTransaction(serializers.Serializer):
#     montant = serializers.FloatField()
#     source = serializers.IntegerField()
#     destination = serializers.IntegerField()
#
#     def create(self, validated_data):
#         transaction = Transaction(
#             montant=validated_data["montant"],
#             source=validated_data["source"],
#             destination=validated_data["destination"],
#         )
#         return transaction.save()

class SerializerRequest(serializers.ModelSerializer):
    class Meta:
        model = Requete
        fields = '__all__'
