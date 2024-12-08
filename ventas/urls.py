# z:\Escritorio\bibliotecaD\bibliotecaD\ventas\urls.py
from django.urls import path
from .views import historial_ventas  # Asegúrate de que esta vista esté correctamente importada

urlpatterns = [
    path('historial/', historial_ventas, name='historial_ventas'),
]