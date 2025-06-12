from django.contrib import admin
from .models import Entrada, Categoria, Autor  # Ajusta los nombres de tus modelos

admin.site.register(Entrada)
admin.site.register(Categoria)
admin.site.register(Autor)