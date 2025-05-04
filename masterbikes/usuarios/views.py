from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import RegistroUsuarioForm, EditarPerfilForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView
from arriendos.models import Arriendo
from reparaciones.models import Reparacion

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            # Redirigir según el rol
            if user.rol == 'CLIENTE':
                return redirect('perfil_cliente')
            elif user.is_staff:
                return redirect('admin:index')
            else:
                return redirect('home')
        else:
            messages.error(request, 'Usuario o contraseña incorrectos')
    
    return render(request, 'usuarios/login.html')

def logout_view(request):
    logout(request)
    return redirect('login')

def registro(request):
    """Vista para el registro de nuevos usuarios."""
    if request.method == 'POST':
        form = RegistroUsuarioForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            if user.rol == 'CLIENTE':
                return redirect('perfil_cliente')
            return redirect('home')
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

@login_required
def perfil_cliente(request):
    """Vista del perfil del cliente"""
    if request.user.rol != 'CLIENTE':
        return redirect('home')
    
    context = {
        'usuario': request.user,
        'arriendos': Arriendo.objects.filter(usuario=request.user),
        'reparaciones': Reparacion.objects.filter(usuario=request.user)
    }
    return render(request, 'usuarios/perfil_cliente.html', context)

class ArriendosClienteListView(LoginRequiredMixin, ListView):
    """Lista de arriendos del cliente"""
    model = Arriendo
    template_name = 'usuarios/arriendos_cliente.html'
    context_object_name = 'arriendos'

    def get_queryset(self):
        if self.request.user.rol != 'CLIENTE':
            return Arriendo.objects.none()
        return Arriendo.objects.filter(usuario=self.request.user)

class ReparacionesClienteListView(LoginRequiredMixin, ListView):
    """Lista de reparaciones del cliente"""
    model = Reparacion
    template_name = 'usuarios/reparaciones_cliente.html'
    context_object_name = 'reparaciones'

    def get_queryset(self):
        if self.request.user.rol != 'CLIENTE':
            return Reparacion.objects.none()
        return Reparacion.objects.filter(usuario=self.request.user)
