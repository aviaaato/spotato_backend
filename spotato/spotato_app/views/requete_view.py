from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_exempt
from rest_framework import serializers, status
from rest_framework.response import Response
from rest_framework.views import APIView

from spotato_app.models import Categorie, Requete, Spotter, Client


class CategorieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categorie
        fields = "__all__"


class GetAllCategorie(APIView):
    def get(self, request):
        all_categorie = Categorie.objects.all()
        categorie = CategorieSerializer(all_categorie, many=True)
        return Response(categorie.data, status=status.HTTP_200_OK)


class RequeteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Requete
        fields = "__all__"


class RequeteInputSerializer(serializers.ModelSerializer):
    class Meta:
        model = Requete
        fields = [
            "label",
            "description",
            "categorie",
            "latitude",
            "longitude",
            "duration",
            "requested_start_time",
            "montant",
        ]


class ManageRequete(APIView):
    def post(self, request):
        """Client create new requete by post method
            - need Client token
        """
        requete_serializer = RequeteInputSerializer(data=request.data)
        if requete_serializer.is_valid():
            if request.user.is_authenticated:
                user = User.objects.get(pk=request.user.id)
                client = Client.objects.filter(user=user)
                data = requete_serializer.validated_data
                if client.exists():

                    # Todo implement Mvola API here
                    # Need payement befor create Requete

                    Requete.objects.create(
                        client=client.first(),
                        description=data["description"],
                        label=data["label"],
                        categorie=data["categorie"],
                        latitude=data["latitude"],
                        longitude=data["longitude"],
                        duration=data["duration"],
                        requested_start_time=data["requested_start_time"],
                        montant=data["montant"],
                    )
                    return Response("Requete is create", status=status.HTTP_201_CREATED)
                else:
                    return Response(
                        "Client is not connected", status=status.HTTP_404_NOT_FOUND
                    )
            else:
                return Response(
                    "User is not authenticate", status=status.HTTP_404_NOT_FOUND
                )

        return Response(requete_serializer.errors, status=status.HTTP_403_FORBIDDEN)

    def get(self, request):
        """ Spotter Get all Requete
            - Need Spotter token
        """
        if request.user.is_authenticated:
            user = User.objects.get(pk=request.user.id)
            if Spotter.objects.filter(user=user).exists():
                list_requete = Requete.objects.filter(status=0)
                list_requete_serializer = RequeteSerializer(list_requete, many=True)
                return Response(list_requete_serializer.data, status=status.HTTP_200_OK)
            else:
                return Response("Spotter not found", status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response(
                "User is not authenticate", status=status.HTTP_400_BAD_REQUEST
            )


@csrf_exempt
def get_requete_detail(request, id_requete):
    if request.method == "GET":
        if request.user.is_authenticated:
            requete = Requete.objects.filter(pk=id_requete, status=0)
            requete_serializer = RequeteSerializer(requete, many=False)
            return Response(requete_serializer.data, status=status.HTTP_200_OK)
        else:
            return Response("User is not authenticate", status=status.HTTP_400_BAD_REQUEST)


class GetClientRequete(APIView):
    def get(self, request):
        if request.user.is_authenticated:
            user = User.objects.get(pk=request.user.id)
            client = Client.objects.filter(user=user)
            if client.exists():
                list_requete = Requete.objects.filter(client=client.first())
                list_requete_serializer = RequeteSerializer(list_requete, many=True)
                return Response(list_requete_serializer.data, status=status.HTTP_200_OK)
            else:
                return Response("Client not found", status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response(
                "User is not authenticate", status=status.HTTP_400_BAD_REQUEST
            )
