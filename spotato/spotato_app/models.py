from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone


class Client(models.Model):
    phone = models.CharField(max_length=10)
    user = models.OneToOneField(User, on_delete=models.DO_NOTHING)


class Spotter(models.Model):
    phone = models.CharField(max_length=10)
    user = models.OneToOneField(User, on_delete=models.DO_NOTHING)


class Categorie(models.Model):
    label = models.CharField(max_length=100)
    icon = models.ImageField()


class Requete(models.Model):
    client = models.ForeignKey(Client, on_delete=models.DO_NOTHING)
    spotter = models.ForeignKey(Spotter, on_delete=models.CASCADE, null=True)
    label = models.CharField(max_length=100)
    description = models.TextField()
    categorie = models.ForeignKey(Categorie, on_delete=models.DO_NOTHING)
    latitude = models.CharField(max_length=100)
    longitude = models.CharField(max_length=100)
    duration = models.FloatField()
    requested_start_time = models.DateTimeField()  # user fix this
    montant = models.FloatField()
    status = models.IntegerField(default=0)
    start_time = models.TimeField(null=True)
    stop_time = models.TimeField(null=True)


class Transaction(models.Model):
    montant = models.FloatField()
    source = models.ForeignKey(User, on_delete=models.DO_NOTHING, related_name='user_transaction_source')
    requete = models.ForeignKey(Requete, on_delete=models.DO_NOTHING, related_name="transaction_requete")
    date_time = models.DateTimeField(default=timezone.now())
