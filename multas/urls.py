from django.urls import path
from .views import mis_multas, pagar_multa, ver_multas, eliminar_multa

urlpatterns = [
    path('mis_multas/', mis_multas, name='mis_multas'),
    path('pagar_multa/<int:multa_id>/', pagar_multa, name='pagar_multa'),
    path('ver_multas/', ver_multas, name='ver_multas'),  # Nueva URL para ver multas
    path('eliminar_multa/<int:multa_id>/', eliminar_multa, name='eliminar_multa'),
]