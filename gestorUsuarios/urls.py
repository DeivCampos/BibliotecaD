from django.urls import path
from django.contrib.auth import views as auth_views
from .views import registro, home, index, gestor_usuarios, editar_usuario, eliminar_usuario # Asegúrate de que la vista de home esté importada

urlpatterns = [
    path('', index, name='index'),
    path('registro/', registro, name='registro'),
    path('login/', auth_views.LoginView.as_view(template_name='gestorUsuarios/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('gestor_usuarios/', gestor_usuarios, name='gestor_usuarios'),  # Nueva URL para listar usuarios
    path('editar_usuario/<int:usuario_id>/', editar_usuario, name='editar_usuario'),  # Nueva URL para editar usuario
    path('eliminar_usuario/<int:usuario_id>/', eliminar_usuario, name='eliminar_usuario'),
]