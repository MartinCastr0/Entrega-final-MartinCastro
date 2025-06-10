from django.urls import path
from . import views

urlpatterns = [
    path('', views.pages_list, name='pages_list'), # Listado de entradas
    path('entrada/<int:pk>/', views.page_detail, name='page_detail'), # Detalle
    path('crear_entrada/', views.crear_entrada, name='crear_entrada'),
    path('editar_entrada/<int:pk>/', views.editar_entrada, name='editar_entrada'),
    path('borrar_entrada/<int:pk>/', views.borrar_entrada, name='borrar_entrada'),
]