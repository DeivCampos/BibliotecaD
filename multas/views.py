from django.shortcuts import render, redirect, get_object_or_404
from .models import Multa
from django.contrib.auth.decorators import login_required

@login_required
def mis_multas(request):
    multas = Multa.objects.filter(usuario=request.user)
    return render(request, 'multas/mis_multas.html', {'multas': multas})

@login_required
def pagar_multa(request, multa_id):
    multa = get_object_or_404(Multa, id=multa_id, usuario=request.user)

    if request.method == 'POST':
        # Cambiar el estado de la multa a 'pagada'
        multa.estado = 'pagada'
        multa.save()
        return redirect('mis_multas')  # Redirigir a la página de mis multas

    return render(request, 'multas/pagar_multa.html', {'multa': multa})

@login_required
def ver_multas(request):
    # Verifica si el usuario es superusuario
    if request.user.is_superuser:
        multas = Multa.objects.all()  # Obtener todas las multas
    else:
        multas = Multa.objects.filter(usuario=request.user)  # Obtener solo las multas del usuario actual

    return render(request, 'multas/ver_multas.html', {'multas': multas})

@login_required
def eliminar_multa(request, multa_id):
    multa = get_object_or_404(Multa, id=multa_id)

    if request.method == 'POST':
        multa.delete()  # Eliminar la multa
        return redirect('ver_multas')  # Redirigir a la página de ver multas

    return render(request, 'multas/eliminar_multa.html', {'multa': multa})