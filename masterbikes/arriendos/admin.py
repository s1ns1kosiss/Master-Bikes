from django.contrib import admin
from .models import Arriendo

@admin.register(Arriendo)
class ArriendoAdmin(admin.ModelAdmin):
    list_display = ('usuario', 'producto', 'fecha_inicio', 'fecha_fin', 'estado', 'total', 'entregado')
    list_filter = ('estado', 'entregado', 'metodo_pago')
    search_fields = ('usuario__username', 'producto__nombre')
