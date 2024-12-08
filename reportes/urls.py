
from django.urls import path
from .views import reportes_generales, libros_mas_solicitados, multas_por_usuario, ventas_realizadas

urlpatterns = [
    path('', reportes_generales, name='reportes_generales'),
    path('libros_mas_solicitados/', libros_mas_solicitados, name='libros_mas_solicitados'),
    path('multas_por_usuario/', multas_por_usuario, name='multas_por_usuario'),
    path('ventas_realizadas/', ventas_realizadas, name='ventas_realizadas'),
]