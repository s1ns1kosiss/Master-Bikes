from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.utils import timezone
from .models import Promocion
from .forms import PromocionForm

# Create your views here.

@login_required
def lista_promociones(request):
    promociones = Promocion.objects.filter(
        fecha_inicio__lte=timezone.now(),
        fecha_fin__gte=timezone.now(),
        activa=True
    ).order_by('-fecha_inicio')
    
    # Filtrar por tipo de cliente
    if request.user.rol != 'SUPERVISOR':
        promociones = promociones.filter(
            tipo_cliente__in=['TODOS', request.user.rol]
        )
    
    return render(request, 'promociones/lista.html', {
        'promociones': promociones
    })

@login_required
def detalle_promocion(request, pk):
    promocion = get_object_or_404(Promocion, pk=pk)
    return render(request, 'promociones/detalle.html', {
        'promocion': promocion
    })

@login_required
def crear_promocion(request):
    if request.user.rol != 'SUPERVISOR':
        messages.error(request, 'No tienes permisos para crear promociones.')
        return redirect('lista_promociones')
    
    if request.method == 'POST':
        form = PromocionForm(request.POST)
        if form.is_valid():
            promocion = form.save()
            messages.success(request, 'Promoción creada exitosamente.')
            return redirect('detalle_promocion', pk=promocion.pk)
    else:
        form = PromocionForm()
    
    return render(request, 'promociones/crear.html', {
        'form': form
    })

@login_required
def editar_promocion(request, pk):
    if request.user.rol != 'SUPERVISOR':
        messages.error(request, 'No tienes permisos para editar promociones.')
        return redirect('lista_promociones')
    
    promocion = get_object_or_404(Promocion, pk=pk)
    
    if request.method == 'POST':
        form = PromocionForm(request.POST, instance=promocion)
        if form.is_valid():
            form.save()
            messages.success(request, 'Promoción actualizada exitosamente.')
            return redirect('detalle_promocion', pk=promocion.pk)
    else:
        form = PromocionForm(instance=promocion)
    
    return render(request, 'promociones/editar.html', {
        'form': form,
        'promocion': promocion
    })

@login_required
def desactivar_promocion(request, pk):
    if request.user.rol != 'SUPERVISOR':
        messages.error(request, 'No tienes permisos para desactivar promociones.')
        return redirect('lista_promociones')
    
    promocion = get_object_or_404(Promocion, pk=pk)
    promocion.activa = False
    promocion.save()
    messages.success(request, 'Promoción desactivada exitosamente.')
    return redirect('lista_promociones')
