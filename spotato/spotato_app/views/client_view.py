from django.contrib.auth.models import User
from rest_framework import serializers, status
from rest_framework.response import Response
from rest_framework.views import APIView

from spotato_app.models import Client


class ClientSerializer(serializers.Serializer):
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
            password=validated_data["paviewssword"],
        )

        return Client.objects.create(user=user, phone=validated_data["phone"])


class ManageClient(APIView):
    def get(self, request):
        """Get user detaille
        print user information
        """
        if request.user.is_authenticated:
            user = User.objects.get(pk=request.user.id)
            client = Client.objects.filter(user=user)
            client_serializer = ClientSerializer(client, many=False)
            return Response(client_serializer.data, status=status.HTTP_200_OK)
        return Response("user not connected", status.HTTP_400_BAD_REQUEST)

    def post(self, request):
        """Create new User
        client register
        """
        client_serializer = ClientSerializer(data=request.data)
        if client_serializer.is_valid():
            if User.objects.filter(
                    username=client_serializer.validated_data["username"]
            ).exists():
                return Response(
                    {"username": ["this username is already used by other client"]},
                    status=status.HTTP_400_BAD_REQUEST,
                )
            client_serializer.save()

            data = {
                "username": client_serializer.validated_data["username"],
                "phone": client_serializer.validated_data["phone"],
            }
            return Response(data, status=status.HTTP_201_CREATED)

        return Response(client_serializer.errors, status=status.HTTP_403_FORBIDDEN)
