from django.urls import path
from rest_framework.authtoken import views

from spotato_app.views import ClientRegisterView, GetClientDetailView, GetClientRequeteView

urlpatterns = [
    path("api/client", ClientRegisterView.as_view()),
    path("api/spotter", ClientRegisterView.as_view()),
    path("api/client/login", views.obtain_auth_token),
    path("api/spotter/login", views.obtain_auth_token),
    path("api/client", GetClientDetailView.as_view()),
    path("api/client/requests", GetClientRequeteView.as_view()),
]
