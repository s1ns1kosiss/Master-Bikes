from django.shortcuts import render, get_object_or_404
from .models import Reparacion

def lista_reparaciones(request):
    """Vista para listar todas las reparaciones."""
    reparaciones = Reparacion.objects.all()
    return render(request, 'reparaciones/lista.html', {'reparaciones': reparaciones})

def nueva_reparacion(request):
    """Vista para crear una nueva reparación."""
    return render(request, 'reparaciones/nueva.html')

def detalle_reparacion(request, reparacion_id):
    """Vista para mostrar el detalle de una reparación."""
    reparacion = get_object_or_404(Reparacion, id=reparacion_id)
    return render(request, 'reparaciones/detalle.html', {'reparacion': reparacion})
