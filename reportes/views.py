# z:\Escritorio\bibliotecaD\bibliotecaD\reportes\views.py
from django.shortcuts import render
from prestamos.models import Prestamo
from catalogo.models import Libro
from multas.models import Multa
from ventas.models import Venta
from django.db.models import Count

def reportes_generales(request):
    prestamos_realizados = Prestamo.objects.count()
    libros_solicitados = Libro.objects.filter(prestamo__isnull=False).count()
    multas_generadas = Multa.objects.count()
    ventas_realizadas = Venta.objects.count()
    
    context = {
        'prestamos_realizados': prestamos_realizados,
        'libros_solicitados': libros_solicitados,
        'multas_generadas': multas_generadas,
        'ventas_realizadas': ventas_realizadas,
    }
    return render(request, 'reportes/reportes.html', context)

def libros_mas_solicitados(request):
    libros = Libro.objects.annotate(num_solicitudes=Count('prestamo')).order_by('-num_solicitudes')[:10]
    return render(request, 'reportes/libros_mas_solicitados.html', {'libros': libros})

def multas_por_usuario(request):
    multas = Multa.objects.values('usuario__username').annotate(total_multas=Count('id')).order_by('-total_multas')
    return render(request, 'reportes/multas_por_usuario.html', {'multas': multas})

def ventas_realizadas(request):
    ventas = Venta.objects.values('libro__titulo').annotate(total_ventas=Count('id')).order_by('-total_ventas')
    return render(request, 'reportes/ventas_realizadas.html', {'ventas': ventas})