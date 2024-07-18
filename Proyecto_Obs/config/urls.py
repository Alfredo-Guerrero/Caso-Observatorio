"""
URL configuration for config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('UsuariosApp.urls')), # URL RAIZ 
    path('UsuariosApp/', include(('UsuariosApp.urls', 'UsuariosApp'), namespace='UsuariosApp')),
    path('PersonasApp/', include(('PersonasApp.urls', 'PersonasApp'), namespace='PersonasApp')),
    path('IncidenciasApp/', include(('IncidenciasApp.urls', 'IncidenciasApp'), namespace='IncidenciasApp')),
] #+ static(settings.STATIC_URL, document_root = settings.STATIC_ROOT)

# Agregar rutas para servir archivos estáticos y multimedia solo durante el desarrollo
if settings.DEBUG:
    
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)