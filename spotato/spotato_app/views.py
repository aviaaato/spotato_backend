from django.views.decorators.csrf import csrf_exempt
from rest_framework import status
from rest_framework.authtoken.admin import User
from rest_framework.response import Response
from rest_framework.views import APIView

from spotato_app.airtel_api import AirtelApi
from spotato_app.models import Spotter, Client, Requete, Categorie, Transaction
from spotato_app.serializer import SerializerClientRegister, SerializerSpotterRegister, SerializerTransaction, \
    SerializerRequest


#
class CategorieDetailleView(APIView):
    def get(self, request):
        categorie = Categorie.objects.all()

        data = {
            "categories": []
        }
        for cat in categorie:
            data["categories"].append({"id": cat.id, "icon": str(cat.icon), "label": cat.label})

        return Response(data, status=status.HTTP_200_OK)


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
        try:
            pk = request.user.id
            user = User.objects.get(pk=pk)
            client = Client.objects.filter(user=user)
            data = {
                "username": user.username,
                "phone": client.phone,
            }
            return Response(data, status=status.HTTP_200_OK)
        except Exception as e:
            return Response(e, status=status.HTTP_403_FORBIDDEN)


class GetClientRequeteView(APIView):
    def get(self, request):
        pk = request.user.id

        user = User.objects.get(pk=pk)
        client = Client.objects.get(user=user)
        list_requete = Requete.objects.filter(client=client)

        serializer = SerializerRequest(list_requete, many=True)

        return Response(serializer.data, status.HTTP_200_OK)


class CreateRequeteView(APIView):
    def post(self, request):
        try:
            inputRequete = request.data
            user = User.objects.get(pk=request.user.id)
            client = Client.objects.get(user=user)
            categorie = Categorie.objects.get(pk=inputRequete.get("categorie"))
            requete = Requete(
                client=client,
                description=inputRequete.get("description"),
                label=inputRequete.get("label"),
                categorie=categorie,
                latitude=inputRequete.get("latitude"),
                longitude=inputRequete.get("longitude"),
                duration=inputRequete.get("duration"),
                requested_start_time=inputRequete.get("requested_start_time"),
                montant=inputRequete.get("montant")
            )
            requete.save()
            return Response("requete is create", status.HTTP_200_OK)
        except Exception as e:
            print("exception: ", e)
            return Response("error", status.HTTP_400_BAD_REQUEST)


class SpotterGetAllRequete(APIView):

    def get(self, request):
        try:
            pk = request.user.id
            user = User.objects.get(pk=pk)
            list_requete = Requete.objects.filter(status=0)
            return Response(list_requete, status=status.HTTP_200_OK)
        except Exception as e:
            print("Get All Error ", e)
            return Response("error", status.HTTP_400_BAD_REQUEST)


@csrf_exempt
def spotter_get_detaille_requete(request, pk):
    if request.user.is_authenticated:
        if request.method == "GET":
            try:
                user = User.objects.get(pk=request.user.id)
                requete = Requete.objects.get(pk)
                return Response(requete, status.HTTP_200_OK)
            except Exception as e:
                print(e)
                return Response("error", status.HTTP_400_BAD_REQUEST)
        elif request.method == "PATCH":
            try:
                user = User.objects.get(pk=request.user.id)
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
                print(e)
                return Response("error", status=status.HTTP_400_BAD_REQUEST)
    return Response("user is not yet authenticate", status=status.HTTP_400_BAD_REQUEST)


class DoTransactionView(APIView):
    def post(self, request):
        transaction_serializer = SerializerTransaction(data=request.data)
        if transaction_serializer.is_valid():
            try:
                user = User.objects.get(pk=request.user.id)
                client = Spotter.objects.get(user=user)  # just catch if spotter is now existe

                requete = Requete.objects.get(client=client, spotter=transaction_serializer["destination"])
                spotter = requete.spotter()

                transaction = Transaction.objects.create(montant=transaction_serializer["montant"], source=client,
                                                         destination=spotter)
                airtel = AirtelApi()
                result_transaction = airtel.payments(client.phone)
                data = {
                    "transaction": transaction,
                    "transaction_response_from_api": result_transaction
                }
                return Response(data, status.HTTP_200_OK)
            except Exception as e:
                print("exception = ", e)
                return Response("error", status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response(transaction_serializer.errors, status=status.HTTP_403_FORBIDDEN)


class CallBack(APIView):
    def get(self):
        pass
