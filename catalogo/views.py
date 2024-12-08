from django.shortcuts import render, redirect, get_object_or_404
from .models import Libro, Autor, Categoria
from .forms import LibroForm, AutorForm, CategoriaForm 
from django.contrib.auth.decorators import login_required
from django.core.exceptions import PermissionDenied

def catalogo_libros(request):
    libros = Libro.objects.all()
    return render(request, 'catalogo/catalogo.html', {'libros': libros})

# Vista para listar libros
def listar_libros(request):
    libros = Libro.objects.all()
    return render(request, 'catalogo/listar_libros.html', {'libros': libros})

# Vista para crear un libro
@login_required
def crear_libro(request):
    if not request.user.is_superuser:  # Verifica si el usuario es superusuario
        raise PermissionDenied  # Lanza un error si no tiene permiso
    if request.method == 'POST':
        form = LibroForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_libros')
    else:
        form = LibroForm()
    return render(request, 'catalogo/crear_libro.html', {'form': form})

@login_required
def editar_libro(request, libro_id):
    if not request.user.is_superuser:  # Verifica si el usuario es superusuario
        raise PermissionDenied  # Lanza un error si no tiene permiso
    libro = get_object_or_404(Libro, id=libro_id)
    if request.method == 'POST':
        form = LibroForm(request.POST, instance=libro)
        if form.is_valid():
            form.save()
            return redirect('listar_libros')
    else:
        form = LibroForm(instance=libro)
    return render(request, 'catalogo/editar_libro.html', {'form': form})

@login_required
def eliminar_libro(request, libro_id):
    if not request.user.is_superuser:  # Verifica si el usuario es superusuario
        raise PermissionDenied  # Lanza un error si no tiene permiso
    libro = get_object_or_404(Libro, id=libro_id)
    if request.method == 'POST':
        libro.delete()
        return redirect('listar_libros')
    return render(request, 'catalogo/eliminar_libro.html', {'libro': libro})

def buscar_libros(request):
    query = request.GET.get('q')
    libros = Libro.objects.all()
    if query:
        libros = libros.filter(titulo__icontains=query)  # Filtra por título
    return render(request, 'catalogo/listar_libros.html', {'libros': libros})