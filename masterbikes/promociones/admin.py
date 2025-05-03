from django.contrib import admin
from .models import Promocion

@admin.register(Promocion)
class PromocionAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'tipo_cliente', 'fecha_inicio', 'fecha_fin', 'activa')
    list_filter = ('tipo_cliente', 'activa')
    search_fields = ('titulo', 'descripcion')
