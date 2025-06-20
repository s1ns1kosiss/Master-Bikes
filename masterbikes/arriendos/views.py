from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Arriendo
from .forms import ArriendoForm
from django.utils import timezone

@login_required
def lista_arriendos(request):
    """Vista para listar todos los arriendos."""
    if request.user.is_staff:
        arriendos = Arriendo.objects.all()
    else:
        arriendos = Arriendo.objects.filter(usuario=request.user)
    return render(request, 'arriendos/lista.html', {'arriendos': arriendos})

@login_required
def nuevo_arriendo(request):
    """Vista para crear un nuevo arriendo."""
    if request.method == 'POST':
        form = ArriendoForm(request.POST)
        if form.is_valid():
            arriendo = form.save(commit=False)
            producto = arriendo.producto
            if producto.stock > 0 and producto.estado == 'DISPONIBLE':
                arriendo.usuario = request.user
                # Calcular total: precio * días
                dias = (arriendo.fecha_fin - arriendo.fecha_inicio).days
                if dias < 1:
                    dias = 1
                arriendo.total = producto.precio * dias
                arriendo.save()
                # Descontar stock
                producto.stock -= 1
                # Cambiar estado si stock llega a 0
                if producto.stock == 0:
                    producto.estado = 'RESERVADO'
                producto.save()
                messages.success(request, 'Arriendo creado exitosamente.')
                return redirect('arriendos:detalle', arriendo_id=arriendo.id)
            else:
                messages.error(request, 'No hay stock disponible para este producto.')
    else:
        form = ArriendoForm()
    return render(request, 'arriendos/form.html', {'form': form})

@login_required
def detalle_arriendo(request, arriendo_id):
    """Vista para mostrar el detalle de un arriendo."""
    arriendo = get_object_or_404(Arriendo, id=arriendo_id)
    if not request.user.is_staff and arriendo.usuario != request.user:
        messages.error(request, 'No tienes permiso para ver este arriendo.')
        return redirect('arriendos:lista')
    return render(request, 'arriendos/detalle.html', {'arriendo': arriendo})

@login_required
def finalizar_arriendo(request, arriendo_id):
    """Vista para finalizar/devolver un arriendo."""
    arriendo = get_object_or_404(Arriendo, id=arriendo_id)
    if not request.user.is_staff:
        messages.error(request, 'No tienes permiso para finalizar este arriendo.')
        return redirect('arriendos:detalle', arriendo_id=arriendo.id)
    if arriendo.estado != 'FINALIZADO':
        producto = arriendo.producto
        producto.stock += 1
        if producto.estado == 'RESERVADO' and producto.stock > 0:
            producto.estado = 'DISPONIBLE'
        producto.save()
        arriendo.estado = 'FINALIZADO'
        arriendo.fecha_devolucion_real = timezone.now()
        arriendo.save()
        messages.success(request, 'Arriendo finalizado y producto devuelto correctamente.')
    else:
        messages.info(request, 'Este arriendo ya está finalizado.')
    return redirect('arriendos:detalle', arriendo_id=arriendo.id)
