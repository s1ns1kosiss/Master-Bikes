from django.shortcuts import render, get_object_or_404
from .models import Producto
from django.db.models import Q
from django.core.paginator import Paginator

def lista_productos(request):
    """Vista para listar todos los productos con opción de ordenamiento, filtros por tipo, estado, búsqueda y paginación."""
    tipo = request.GET.get('tipo', '')
    estado = request.GET.get('estado', '')
    orden = request.GET.get('orden', 'nombre_asc')
    q = request.GET.get('q', '').strip()
    productos = Producto.objects.all()
    if tipo:
        productos = productos.filter(tipo=tipo)
    if estado:
        productos = productos.filter(estado=estado)
    if q:
        productos = productos.filter(Q(nombre__icontains=q) | Q(marca__icontains=q))
    if orden == 'precio_asc':
        productos = productos.order_by('precio')
    elif orden == 'precio_desc':
        productos = productos.order_by('-precio')
    elif orden == 'stock_asc':
        productos = productos.order_by('stock')
    elif orden == 'stock_desc':
        productos = productos.order_by('-stock')
    elif orden == 'nombre_desc':
        productos = productos.order_by('-nombre')
    else:  # nombre_asc por defecto
        productos = productos.order_by('nombre')
    paginator = Paginator(productos, 8)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'productos/lista.html', {
        'productos': page_obj.object_list,
        'page_obj': page_obj,
        'orden': orden,
        'tipo': tipo,
        'estado': estado,
        'q': q
    })

def detalle_producto(request, producto_id):
    """Vista para mostrar el detalle de un producto."""
    producto = get_object_or_404(Producto, id=producto_id)
    descripcion_bullets = None
    if producto.descripcion:
        # Separar por saltos de línea y luego por puntos
        lineas = producto.descripcion.splitlines()
        bullets = []
        for linea in lineas:
            frases = [f.strip() for f in linea.split('.') if f.strip()]
            bullets.extend(frases)
        if len(bullets) > 1:
            descripcion_bullets = bullets
    return render(request, 'productos/detalle.html', {
        'producto': producto,
        'descripcion_bullets': descripcion_bullets
    })
