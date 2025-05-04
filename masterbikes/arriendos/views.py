from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Arriendo
from .forms import ArriendoForm

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
            arriendo.usuario = request.user
            arriendo.save()
            messages.success(request, 'Arriendo creado exitosamente.')
            return redirect('arriendos:detalle', arriendo_id=arriendo.id)
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
