from django.contrib.auth.models import AbstractUser  
from django.db import models

class User(AbstractUser ):
    ROLE_CHOICES = [
        ('admin', 'Administrador'),
        ('docente', 'Docente'),
        ('alumno', 'Alumno'),
    ]
    role = models.CharField(max_length=10, choices=ROLE_CHOICES, default='alumno')

    # Agrega los related_name para evitar conflictos
    groups = models.ManyToManyField(
        'auth.Group',
        related_name='gestorusuarios_user_set',  # Cambia el related_name
        blank=True,
        help_text='The groups this user belongs to. A user will get all permissions '
                  'granted to each of their groups.',
        verbose_name='groups'
    )
    
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='gestorusuarios_user_set',  # Cambia el related_name
        blank=True,
        help_text='Specific permissions for this user.',
        verbose_name='user permissions'
    )