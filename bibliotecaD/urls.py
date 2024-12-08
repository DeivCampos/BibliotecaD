"""
URL configuration for bibliotecaD project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.views.generic import RedirectView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('usuarios/', include('gestorUsuarios.urls')),
    path('catalogo/', include('catalogo.urls')),
    path('prestamos/', include('prestamos.urls')),
    path('reservas/', include('reservas.urls')),
    path('multas/', include('multas.urls')),
    path('ventas/', include('ventas.urls')),
    path('reportes/', include('reportes.urls')),
    path('', RedirectView.as_view(url='/usuarios/login/')),  # Redirige a la página de inicio de sesión
]