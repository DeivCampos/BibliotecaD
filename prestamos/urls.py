from django.urls import path
from .views import historial_prestamos, realizar_prestamo, devolver_prestamo

urlpatterns = [
    path('historial/', historial_prestamos, name='historial_prestamos'),
    path('realizar_prestamo/<int:libro_id>/', realizar_prestamo, name='realizar_prestamo'),
    path('devolver_prestamo/<int:prestamo_id>/', devolver_prestamo, name='devolver_prestamo'),
]