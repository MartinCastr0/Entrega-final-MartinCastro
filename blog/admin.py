from django.contrib import admin
from .models import Autor, Categoria, Entrada, Jugador, Torneo
from .models import Pareja

admin.site.register(Pareja)
admin.site.register(Autor)
admin.site.register(Categoria)
admin.site.register(Entrada)
admin.site.register(Jugador)
admin.site.register(Torneo)