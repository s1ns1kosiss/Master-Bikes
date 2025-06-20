from django.contrib import admin
from .models import Producto

@admin.register(Producto)
class ProductoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'tipo', 'estado', 'marca', 'precio', 'stock', 'fecha_creacion')
    list_filter = ('tipo', 'estado', 'marca')
    search_fields = ('nombre', 'marca', 'modelo', 'tipo_accesorio')
