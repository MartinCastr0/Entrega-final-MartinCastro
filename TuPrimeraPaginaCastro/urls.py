from django.urls import path
from . import views
from accounts import views as accounts_views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('login/', accounts_views.login_view, name='login'),
    path('signup/', accounts_views.signup, name='signup'),
   # path('entradas/', views.entradas, name='pages_list'),#
]