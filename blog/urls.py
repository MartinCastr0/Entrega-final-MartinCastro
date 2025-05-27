from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('crear_autor/', views.crear_autor, name='crear_autor'),
    path('crear_categoria/', views.crear_categoria, name='crear_categoria'),
    path('crear_entrada/', views.crear_entrada, name='crear_entrada'),
    path('buscar_entrada/', views.buscar_entrada, name='buscar_entrada'),
]