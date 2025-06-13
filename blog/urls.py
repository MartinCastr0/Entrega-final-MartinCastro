from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('crear_autor/', views.crear_autor, name='crear_autor'),
    path('crear_categoria/', views.crear_categoria, name='crear_categoria'),
    path('crear_entrada/', views.crear_entrada, name='crear_entrada'),
    path('buscar_entrada/', views.buscar_entrada, name='buscar_entrada'),
    path('jugadores/', views.jugadores_list, name='jugadores_list'),
    path('crear_jugador/', views.crear_jugador, name='crear_jugador'),
    path('torneos/', views.torneos_list, name='torneos_list'),
    path('crear_torneo/', views.crear_torneo, name='crear_torneo'),
    path('torneo/<int:pk>/', views.torneo_detail, name='torneo_detail'),

    # Aquí agregas la ruta para pages
    path('pages/', views.pages_list, name='pages_list'),
    path('page/<int:pk>/', views.page_detail, name='page_detail'),
    path('page/create/', views.page_create, name='page_create'),
    path('page/<int:pk>/edit/', views.page_update, name='page_update'),
    path('page/<int:pk>/delete/', views.page_delete, name='page_delete'),

    # Editar y borrar entradas adicionales si lo necesitas
    path('entrada/<int:pk>/editar/', views.editar_entrada, name='editar_entrada'),
    path('entrada/<int:pk>/borrar/', views.borrar_entrada, name='borrar_entrada'),
]