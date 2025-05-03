from django.contrib import admin
from .models import Producto

@admin.register(Producto)
class ProductoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'tipo', 'marca', 'precio', 'stock', 'fecha_creacion')
    list_filter = ('tipo', 'marca')
    search_fields = ('nombre', 'marca', 'modelo', 'tipo_accesorio')
