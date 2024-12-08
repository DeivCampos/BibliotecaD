from django.db import models
from gestorUsuarios.models import User
from catalogo.models import Libro

class Prestamo(models.Model):
    ESTADO_CHOICES = [
        ('activo', 'Activo'),
        ('devuelto', 'Devuelto'),
    ]
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    libro = models.ForeignKey(Libro, on_delete=models.CASCADE)
    fecha_prestamo = models.DateField(auto_now_add=True)
    fecha_vencimiento = models.DateField()
    estado = models.CharField(max_length=20, choices=ESTADO_CHOICES)
    fecha_devolucion = models.DateField(null=True, blank=True)  # Agregar este campo si no existe

class Devolucion(models.Model):
    prestamo = models.OneToOneField(Prestamo, on_delete=models.CASCADE)
    fecha_devolucion = models.DateField()
    multa = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)