from django.urls import path
from .views import PageListView, PageDetailView, PageCreateView
from . import views

urlpatterns = [
    # Listado de páginas con CBV
    path('pages/', PageListView.as_view(), name='pages_list'),
    # Detalle de página con CBV
    path('pages/<int:pk>/', PageDetailView.as_view(), name='page_detail'),

    # Crear página con CBV + LoginRequiredMixin
    path('pages/create/', PageCreateView.as_view(), name='page_create'),

    # Si quieres dejar las funciones viejas, déjalas con otras rutas:
    path('entrada/<int:pk>/', views.page_detail, name='entrada_page_detail'),  # (Opcional)
    path('crear_entrada/', views.crear_entrada, name='crear_entrada'),
    path('editar_entrada/<int:pk>/', views.editar_entrada, name='editar_entrada'),
    path('borrar_entrada/<int:pk>/', views.borrar_entrada, name='borrar_entrada'),
]