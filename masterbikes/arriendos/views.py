from django.shortcuts import render, get_object_or_404
from .models import Arriendo

def lista_arriendos(request):
    """Vista para listar todos los arriendos."""
    arriendos = Arriendo.objects.all()
    return render(request, 'arriendos/lista.html', {'arriendos': arriendos})

def nuevo_arriendo(request):
    """Vista para crear un nuevo arriendo."""
    return render(request, 'arriendos/nuevo.html')

def detalle_arriendo(request, arriendo_id):
    """Vista para mostrar el detalle de un arriendo."""
    arriendo = get_object_or_404(Arriendo, id=arriendo_id)
    return render(request, 'arriendos/detalle.html', {'arriendo': arriendo})
