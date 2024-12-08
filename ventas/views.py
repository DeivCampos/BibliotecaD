from django.shortcuts import render
from .models import Venta

def historial_ventas(request):
    ventas = Venta.objects.filter(usuario=request.user)
    return render(request, 'ventas/historial.html', {'ventas': ventas})