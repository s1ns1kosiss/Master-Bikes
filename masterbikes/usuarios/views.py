from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import RegistroUsuarioForm, EditarPerfilForm

def registro(request):
    """Vista para el registro de nuevos usuarios."""
    if request.method == 'POST':
        form = RegistroUsuarioForm(request.POST)
        if form.is_valid():
            usuario = form.save()
            messages.success(request, '¡Registro exitoso! Ahora puedes iniciar sesión.')
            return redirect('login')
    else:
        form = RegistroUsuarioForm()
    return render(request, 'usuarios/registro.html', {'form': form})

@login_required
def perfil(request):
    """Vista para ver el perfil del usuario."""
    return render(request, 'usuarios/perfil.html')

@login_required
def editar_perfil(request):
    """Vista para editar el perfil del usuario."""
    if request.method == 'POST':
        form = EditarPerfilForm(request.POST, request.FILES, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, 'Perfil actualizado exitosamente.')
            return redirect('usuarios:perfil')
    else:
        form = EditarPerfilForm(instance=request.user)
    return render(request, 'usuarios/editar_perfil.html', {'form': form})
