from django.urls import path
from .views import listar_libros, crear_libro, editar_libro, eliminar_libro, buscar_libros

urlpatterns = [
    path('libros/', listar_libros, name='listar_libros'),
    path('libros/crear/', crear_libro, name='crear_libro'),
    path('libros/buscar/', buscar_libros, name='buscar_libros'),
    path('libros/editar/<int:libro_id>/', editar_libro, name='editar_libro'),
    path('libros/eliminar/<int:libro_id>/', eliminar_libro, name='eliminar_libro'),
]