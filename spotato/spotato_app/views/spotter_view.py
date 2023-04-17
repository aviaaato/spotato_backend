from django.contrib.auth.models import User
from rest_framework import status, serializers
from rest_framework.response import Response
from rest_framework.views import APIView

from spotato_app.models import Spotter
from spotato_app.views.client_view import UserClientRegisterSerializer


class UserSpotterRegisterSerializer(UserClientRegisterSerializer):
    def create(self, validated_data):
        user = User.objects.create_user(
            first_name=validated_data["first_name"],
            last_name=validated_data["last_name"],
            email=validated_data["email"],
            username=validated_data["username"],
            password=validated_data["password"],
        )
        return Spotter.objects.create(user=user, phone=validated_data["phone"])


class SpotterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Spotter
        fields = "__all__"


class ManageSpotter(APIView):
    def get(self, request):
        """Get Spotter Detaille With Solde"""
        if request.user.is_authenticated:
            user = User.objects.get(pk=request.user.id)
            spotter = Spotter.objects.filter(user=user)
            if spotter.exists():
                spotter_serializer = SpotterSerializer(spotter)
                return Response(spotter_serializer.data, status=status.HTTP_200_OK)
            else:
                return Response(
                    "spotter is not connected", status=status.HTTP_400_BAD_REQUEST
                )
        return Response("User is not connected", status=status.HTTP_400_BAD_REQUEST)

    def post(self, request):
        spotter_serializer = UserSpotterRegisterSerializer(data=request.data)
        if spotter_serializer.is_valid():
            if User.objects.filter(
                    username=spotter_serializer.validated_data["username"]
            ).exists():
                return Response(
                    {"username": ["this username is already used by other spotter"]},
                    status=status.HTTP_400_BAD_REQUEST,
                )
            spotter_serializer.save()
            data = {
                "username": spotter_serializer.validated_data["username"],
                "phone": spotter_serializer.validated_data["phone"],
            }
            return Response(data, status=status.HTTP_201_CREATED)
        return Response(spotter_serializer.errors, status=status.HTTP_403_FORBIDDEN)
