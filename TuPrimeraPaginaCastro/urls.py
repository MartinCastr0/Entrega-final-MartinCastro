from django.urls import path, include
from . import views
from accounts import views as accounts_views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('login/', accounts_views.login_view, name='login'),
    path('signup/', accounts_views.signup, name='signup'),
    path('', include('blog.urls')),
    path('admin/', admin.site.urls),

]

# fotos de jugadores, etc.
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATICFILES_DIRS[0])