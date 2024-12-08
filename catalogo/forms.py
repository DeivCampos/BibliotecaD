from django import forms
from .models import Libro, Autor, Categoria

from django import forms
from .models import Libro, Autor, Categoria

class LibroForm(forms.ModelForm):
    autor_nombre = forms.CharField(max_length=100, label='Nombre del Autor')
    categoria_nombre = forms.CharField(max_length=100, label='Nombre de la Categoría')

    class Meta:
        model = Libro
        fields = ['titulo', 'isbn', 'cantidad_disponible', 'descripcion', 'precio']

    def save(self, commit=True):
        # Primero, obtenemos o creamos el autor
        autor_nombre = self.cleaned_data['autor_nombre']
        autor, created = Autor.objects.get_or_create(nombre=autor_nombre)

        # Luego, obtenemos o creamos la categoría
        categoria_nombre = self.cleaned_data['categoria_nombre']
        categoria, created = Categoria.objects.get_or_create(nombre=categoria_nombre)

        # Creamos el libro
        libro = super().save(commit=False)
        libro.autor = autor
        libro.categoria = categoria

        if commit:
            libro.save()
        return libro

class AutorForm(forms.ModelForm):
    class Meta:
        model = Autor
        fields = ['nombre', 'biografia']

class CategoriaForm(forms.ModelForm):
    class Meta:
        model = Categoria
        fields = ['nombre', 'descripcion']