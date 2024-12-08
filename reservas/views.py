from django.shortcuts import render, redirect, get_object_or_404
from .models import Reserva
from catalogo.models import Libro
from django.contrib.auth.decorators import login_required
@login_required
def mis_reservas(request):
    reservas = Reserva.objects.filter(usuario=request.user)
    return render(request, 'reservas/mis_reservas.html', {'reservas': reservas})


@login_required
def realizar_reserva(request, libro_id):
    libro = get_object_or_404(Libro, id=libro_id)

    if request.method == 'POST':
        # Crear la reserva
        reserva = Reserva(usuario=request.user, libro=libro)
        reserva.save()
        return redirect('mis_reservas')  # Redirige a la página de mis reservas

    return render(request, 'reservas/realizar_reserva.html', {'libro': libro})

@login_required
def ver_reservas(request):
    # Verifica si el usuario es superusuario
    if request.user.is_superuser:
        reservas = Reserva.objects.all()  # Obtener todas las reservas
    else:
        reservas = Reserva.objects.filter(usuario=request.user)  # Obtener solo las reservas del usuario actual

    return render(request, 'reservas/ver_reservas.html', {'reservas': reservas})

@login_required
def eliminar_reserva(request, reserva_id):
    reserva = get_object_or_404(Reserva, id=reserva_id)

    if request.method == 'POST':
        reserva.delete()  # Eliminar la reserva
        return redirect('ver_reservas')  # Redirigir a la página de ver reservas

    return render(request, 'reservas/eliminar_reserva.html', {'reserva': reserva})