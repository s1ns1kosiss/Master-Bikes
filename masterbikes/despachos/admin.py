from django.contrib import admin
from .models import Despacho

@admin.register(Despacho)
class DespachoAdmin(admin.ModelAdmin):
    list_display = ('arriendo', 'direccion_entrega', 'fecha_despacho', 'estado', 'encargado')
    list_filter = ('estado', 'encargado')
    search_fields = ('arriendo__producto__nombre', 'arriendo__usuario__username', 'direccion_entrega')
