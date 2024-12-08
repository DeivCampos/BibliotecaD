from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, authenticate
from django import forms
from .models import User
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model

User  = get_user_model()

@login_required
def gestor_usuarios(request):
    if not request.user.is_superuser:
        return redirect('index')  # Redirigir si no es superusuario

    usuarios = User.objects.all()  # Obtener todos los usuarios
    return render(request, 'gestorUsuarios/gestor_usuarios.html', {'usuarios': usuarios})

class UserCreationFormWithRole(forms.ModelForm):
    password1 = forms.CharField(label='Contraseña', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Confirmar Contraseña', widget=forms.PasswordInput)
    role = forms.ChoiceField(choices=[('docente', 'Docente'), ('alumno', 'Alumno')], label='Rol')

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2', 'role')

    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Las contraseñas no coinciden")
        return password2

def registro(request):
    if request.method == 'POST':
        form = UserCreationFormWithRole(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password1'])
            user.save()
            # Agregar un mensaje de éxito
            messages.success(request, 'Usuario registrado con éxito. Puedes iniciar sesión ahora.')
            return redirect('login')  # Redirige a la página de inicio de sesión
    else:
        form = UserCreationFormWithRole()
    return render(request, 'gestorUsuarios/registro.html', {'form': form})
def home(request):
    return render(request, 'gestorUsuarios/home.html')

@login_required
def index(request):
    if request.user.is_superuser:  # Verifica si es superusuario
        return render(request, 'gestorUsuarios/index_admin.html')
    elif request.user.role == 'admin':
        return render(request, 'gestorUsuarios/index_admin.html')
    else:
        return render(request, 'gestorUsuarios/index_user.html')
    

class UserEditForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'role']  # Campos que deseas permitir editar

@login_required
def editar_usuario(request, usuario_id):
    usuario = get_object_or_404(User, id=usuario_id)

    if request.method == 'POST':
        form = UserEditForm(request.POST, instance=usuario)
        if form.is_valid():
            form.save()  # Guardar los cambios
            return redirect('gestor_usuarios')  # Redirigir a la lista de usuarios
    else:
        form = UserEditForm(instance=usuario)

    return render(request, 'gestorUsuarios/editar_usuario.html', {'form': form, 'usuario': usuario})

@login_required
def eliminar_usuario(request, usuario_id):
    usuario = get_object_or_404(User, id=usuario_id)

    if request.method == 'POST':
        usuario.delete()  # Eliminar el usuario
        return redirect ('gestor_usuarios')  # Redirigir a la lista de usuarios

    return render(request, 'gestorUsuarios/eliminar_usuario.html', {'usuario': usuario})