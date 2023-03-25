from django.views.decorators.csrf import csrf_exempt
from rest_framework import status, viewsets
from rest_framework.authtoken.admin import User
from rest_framework.response import Response
from rest_framework.views import APIView

from spotato_app.models import Spotter, Client, Requete, Categorie
from spotato_app.serializer import SerializerClientRegister, SerializerSpotterRegister, SerializerInputRequete, \
    SerializerCategorie


class CategorieDetailleView(viewsets.ModelViewSet):
    queryset = Categorie.objects.all()
    serializer_class = SerializerCategorie


class ClientRegisterView(APIView):
    def post(self, request):
        client_serializer = SerializerClientRegister(data=request.data)

        if client_serializer.is_valid():
            if User.objects.filter(username=client_serializer.validated_data["username"]).exists():
                return Response({"username": ["this username is already used"]}, status=status.HTTP_400_BAD_REQUEST)
            client_serializer.save()

            data = {
                "username": client_serializer.validated_data["username"],
                "phone": client_serializer.validated_data["phone"]
            }

            return Response(data, status=status.HTTP_201_CREATED)

        return Response(client_serializer.errors, status=status.HTTP_403_FORBIDDEN)


class SpotterRegisterView(APIView):
    def post(self, request):
        spotter_serializer = SerializerSpotterRegister(data=request.data)
        if spotter_serializer.is_valid():
            if Spotter.objects.filter(username=spotter_serializer.validated_data["username"]).exists():
                return Response({"username": ["this username is already used"]}, status=status.HTTP_400_BAD_REQUEST)
            spotter_serializer.save()
            data = {
                "username": spotter_serializer.validated_data["username"],
                "phone": spotter_serializer.validated_data["phone"]
            }
            return Response(data, status=status.HTTP_201_CREATED)
        return Response(spotter_serializer.errors, status=status.HTTP_403_FORBIDDEN)


class GetClientDetailView(APIView):
    def get(self, request):
        if request.user.is_authenticated():
            user = User.objects.get(pk=request.user.id)
            client = Client.objects.filter(user=user)
            data = {
                "username": user.username,
                "phone": client.phone,
            }
            return Response(data, status=status.HTTP_200_OK)
        return Response("user is not yet authenticate", status=status.HTTP_400_BAD_REQUEST)


class GetClientRequeteView(APIView):
    def get(self, request):
        if request.user.is_authenticated():
            user = User.objects.get(pk=request.user.id)
            list_requete = Requete.objects.filter(user=user)
            data = {
                "list_requete": list_requete
            }
            return Response(data, status=status.HTTP_200_OK)
        return Response("user is not yet authenticate", status=status.HTTP_400_BAD_REQUEST)


class CreateRequeteView(APIView):
    def post(self, request):
        inputRequete = SerializerInputRequete(data=request)
        if request.user.is_authenticated() and inputRequete.is_valid():
            try:
                user = User.objects.get(pk=request.user.id)
                client = Client.objects.get(user=user)
                categorie = Categorie.objects.get(pk=inputRequete.categorie)
                requete = Requete(
                    client=client,
                    description=inputRequete.description,
                    lable=inputRequete.label,
                    categorie=categorie,
                    latitude=inputRequete.latitude,
                    longitude=inputRequete.longitude,
                    duration=inputRequete.duration,
                    requested_start_time=inputRequete.requested_start_time,
                    montant=inputRequete.montant,
                )
                requete.save()
                return Response("requete is create", status.HTTP_200_OK)
            except Exception as e:
                return Response(e, status.HTTP_400_BAD_REQUEST)
        return Response("user is not yet authenticate", status=status.HTTP_400_BAD_REQUEST)


class SpotterGetAllRequete(APIView):
    def get(self, request):
        if request.user.is_authenticated():
            try:
                user = User.objects.get(pk=request.user.id)
                _ = Spotter.objects.get(user=user)
                list_requete = Requete.objects.filter(status=0)
                return Response(list_requete, status=status.HTTP_200_OK)
            except Exception as e:
                return Response(e, status.HTTP_400_BAD_REQUEST)
        return Response("user is not yet authenticate", status=status.HTTP_400_BAD_REQUEST)


@csrf_exempt
def spotter_get_detaille_requete(request, pk):
    if request.user.is_authenticated():
        if request.method == "GET":
            try:
                user = User.objects.get(pk=request.user.id)
                _ = Spotter.objects.get(user=user)
                requete = Requete.objects.get(pk)
                return Response(requete, status.HTTP_200_OK)
            except Exception as e:
                return Response(e, status.HTTP_400_BAD_REQUEST)
        elif request.method == "PATCH":
            try:
                user = User.objects.get(pk=request.user.id)
                _ = Spotter.objects.get(user=user)  # just catch if spotter is now existe
                requete = Requete.objects.get(pk)
                requete_status = request.data.get("status", None)
                if requete_status == "start":
                    requete.status = 1
                elif requete_status == "start-chrono":
                    start_time = request.data.get("start_time", None)
                    requete.status = 2
                    requete.start_time = start_time
                else:
                    pass
                requete.save()
                return Response(requete, status.HTTP_200_OK)
            except Exception as e:
                return Response(e, status=status.HTTP_400_BAD_REQUEST)
    return Response("user is not yet authenticate", status=status.HTTP_400_BAD_REQUEST)
