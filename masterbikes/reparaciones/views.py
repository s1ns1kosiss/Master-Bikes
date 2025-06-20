from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Reparacion
from .forms import ReparacionForm, ReparacionStaffForm

@login_required
def lista_reparaciones(request):
    """Vista para listar todas las reparaciones."""
    if request.user.is_staff:
        reparaciones = Reparacion.objects.all()
    else:
        reparaciones = Reparacion.objects.filter(usuario=request.user)
    return render(request, 'reparaciones/lista.html', {'reparaciones': reparaciones})

@login_required
def nueva_reparacion(request):
    """Vista para crear una nueva reparación."""
    if request.method == 'POST':
        form = ReparacionStaffForm(request.POST) if request.user.is_staff else ReparacionForm(request.POST)
        if form.is_valid():
            reparacion = form.save(commit=False)
            reparacion.usuario = request.user
            reparacion.save()
            # Cambiar estado del producto a EN_REPARACION
            producto = reparacion.producto
            producto.estado = 'EN_REPARACION'
            producto.save()
            messages.success(request, 'Reparación creada exitosamente.')
            return redirect('reparaciones:detalle', reparacion_id=reparacion.id)
    else:
        form = ReparacionStaffForm() if request.user.is_staff else ReparacionForm()
    return render(request, 'reparaciones/form.html', {'form': form})

@login_required
def detalle_reparacion(request, reparacion_id):
    """Vista para mostrar el detalle de una reparación."""
    reparacion = get_object_or_404(Reparacion, id=reparacion_id)
    if not request.user.is_staff and reparacion.usuario != request.user:
        messages.error(request, 'No tienes permiso para ver esta reparación.')
        return redirect('reparaciones:lista')
    return render(request, 'reparaciones/detalle.html', {'reparacion': reparacion})
