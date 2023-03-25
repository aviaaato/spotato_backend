from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.views import APIView

from .serializer import *


# Create your views here.

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class ClientViewSet(viewsets.ModelViewSet):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer


class ClientRegisterView(APIView):
    def post(self, request):
        client_serializer = RegisterClientSerializer(data=request.data)

        if client_serializer.is_valid():
            if User.objects.filter(username=client_serializer.validated_data["username"]).exists():
                return Response({"email": ["this username is already used"]}, status=status.HTTP_400_BAD_REQUEST)
            client_serializer.save()

            data = {
                "username": client_serializer.validated_data["username"],
                "phone": client_serializer.validated_data["phone"]
            }

            return Response(data, status=status.HTTP_201_CREATED)

        return Response(client_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
