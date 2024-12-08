from django.shortcuts import render, redirect, get_object_or_404
from .models import Prestamo
from catalogo.models import Libro
from django.contrib.auth.decorators import login_required
from django.core.exceptions import PermissionDenied
from django.utils import timezone
from datetime import timedelta

def historial_prestamos(request):
    prestamos = Prestamo.objects.filter(usuario=request.user)
    return render(request, 'prestamos/historial.html', {'prestamos': prestamos})

@login_required
def realizar_prestamo(request, libro_id):
    libro = get_object_or_404(Libro, id=libro_id)
    
    if request.method == 'POST':
        # Verificar si el libro está disponible
        if libro.cantidad_disponible > 0:
            # Crear el préstamo
            prestamo = Prestamo(usuario=request.user, libro=libro)
            prestamo.fecha_vencimiento = timezone.now() + timedelta(days=14)  # Por ejemplo, 14 días de préstamo
            prestamo.estado = 'activo'  # Asegúrate de establecer el estado aquí
            prestamo.save()
            # Disminuir la cantidad disponible del libro
            libro.cantidad_disponible -= 1
            libro.save()
            return redirect('historial_prestamos')  # Redirige al historial de préstamos
        else:
            # Manejar el caso en que no hay copias disponibles
            return render(request, 'prestamos/error.html', {'mensaje': 'No hay copias disponibles para este libro.'})
    
    return render(request, 'prestamos/realizar_prestamo.html', {'libro': libro})

@login_required
def historial_prestamos(request):
    # Si el usuario es superusuario, mostrar todos los préstamos
    if request.user.is_superuser:
        prestamos = Prestamo.objects.all()  # Obtener todos los préstamos
    else:
        prestamos = Prestamo.objects.filter(usuario=request.user)  # Obtener solo los préstamos del usuario actual

    return render(request, 'prestamos/historial_prestamos.html', {'prestamos': prestamos})

@login_required
def devolver_prestamo(request, prestamo_id):
    prestamo = get_object_or_404(Prestamo, id=prestamo_id, usuario=request.user)

    if request.method == 'POST':
        # Cambiar el estado del préstamo a devuelto
        prestamo.estado = 'devuelto'  # Asegúrate de que el estado se actualice aquí
        prestamo.fecha_devolucion = timezone.now()  # Registrar la fecha de devolución
        prestamo.save()

        return redirect('historial_prestamos')  # Redirige al historial de préstamos

    return render(request, 'prestamos/devolver_prestamo.html', {'prestamo': prestamo})