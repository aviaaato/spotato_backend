from django.shortcuts import render, HttpResponse
from rest_framework import viewsets
from django.contrib.auth.models import User
from .models import *
from .serializer import *
# Create your views here.

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class ClientViewSet(viewsets.ModelViewSet):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer