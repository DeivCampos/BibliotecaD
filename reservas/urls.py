from django.urls import path
from .views import mis_reservas, realizar_reserva, ver_reservas, eliminar_reserva

urlpatterns = [
    path('mis_reservas/', mis_reservas, name='mis_reservas'),
    path('reservar/<int:libro_id>/', realizar_reserva, name='realizar_reserva'),
    path('ver_reservas/', ver_reservas, name='ver_reservas'),  # URL para ver reservas
    path('eliminar_reserva/<int:reserva_id>/', eliminar_reserva, name='eliminar_reserva'),  # Nueva URL para eliminar reserva
]