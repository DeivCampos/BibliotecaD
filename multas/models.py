from django.db import models
from gestorUsuarios.models import User
from prestamos.models import Prestamo

class Multa(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    prestamo = models.ForeignKey(Prestamo, on_delete=models.CASCADE)
    monto = models.DecimalField(max_digits=10, decimal_places=2)
    estado = models.CharField(max_length=20, choices=[('pendiente', 'Pendiente'), ('pagada', 'Pagada')])