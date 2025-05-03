from django.shortcuts import render, get_object_or_404
from .models import Producto

def lista_productos(request):
    """Vista para listar todos los productos."""
    productos = Producto.objects.all()
    return render(request, 'productos/lista.html', {'productos': productos})

def detalle_producto(request, producto_id):
    """Vista para mostrar el detalle de un producto."""
    producto = get_object_or_404(Producto, id=producto_id)
    return render(request, 'productos/detalle.html', {'producto': producto})
