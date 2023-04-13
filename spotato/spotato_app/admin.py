from django.contrib import admin

from spotato_app.models import Spotter, Categorie, Requete, Client, Transaction

admin.site.register(Spotter)
admin.site.register(Categorie)
admin.site.register(Requete)
admin.site.register(Client)
admin.site.register(Transaction)
