from django.contrib import admin
from .models import Promocion

@admin.register(Promocion)
class PromocionAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'tipo_cliente', 'fecha_inicio', 'fecha_fin', 'descuento', 'activa')
    list_filter = ('tipo_cliente', 'activa', 'fecha_inicio', 'fecha_fin')
    search_fields = ('titulo', 'descripcion')
    date_hierarchy = 'fecha_inicio'
    filter_horizontal = ('productos', 'usuarios_destinatarios')
    readonly_fields = ('fecha_creacion',)
    
    fieldsets = (
        ('Información Básica', {
            'fields': ('titulo', 'descripcion', 'tipo_cliente', 'descuento')
        }),
        ('Fechas', {
            'fields': ('fecha_inicio', 'fecha_fin', 'fecha_creacion')
        }),
        ('Estado', {
            'fields': ('activa',)
        }),
        ('Productos y Usuarios', {
            'fields': ('productos', 'usuarios_destinatarios'),
            'classes': ('collapse',)
        }),
    )
