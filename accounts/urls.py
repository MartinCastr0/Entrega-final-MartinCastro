from django.urls import path
from django.contrib.auth import views as auth_views
from . import views
from blog import views as blog_views

urlpatterns = [
    path('signup/', views.signup, name='signup'),
    path('login/', auth_views.LoginView.as_view(template_name='accounts/login.html'), name='login'),
    path('accounts/login/', blog_views.tu_vista_de_login, name='login'),
]