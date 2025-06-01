from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('movies.urls')),
]

# Configuración para servir archivos estáticos y multimedia en desarrollo
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    # La carpeta donde se guardarán los archivos multimedia subidos por el usuario
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
