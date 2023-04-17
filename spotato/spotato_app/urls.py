from django.urls import path
from rest_framework.authtoken import views

from spotato_app.views.client_view import ManageClient
from spotato_app.views.requete_view import requete_detail, ManageRequete, \
    GetAllCategorie
from spotato_app.views.spotter_view import ManageSpotter

urlpatterns = [
    path("api/client", ManageClient.as_view()),
    path("api/client/login", views.obtain_auth_token),
    path("api/spotter", ManageSpotter.as_view()),
    path("api/spotter/login", views.obtain_auth_token),
    path("api/categorie", GetAllCategorie.as_view()),
    path("api/requete", ManageRequete.as_view()),
    path("api/requete/<int:id_requete>", requete_detail),
]
