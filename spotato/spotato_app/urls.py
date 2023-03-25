from django.urls import path
from rest_framework.authtoken import views

from spotato_app.views import ClientRegisterView

urlpatterns = [
    path("api/users", ClientRegisterView.as_view()),
    path("api/login", views.obtain_auth_token)
]
