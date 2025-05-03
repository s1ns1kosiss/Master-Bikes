from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Usuario

@admin.register(Usuario)
class UsuarioAdmin(UserAdmin):
    model = Usuario
    list_display = ('username', 'email', 'nombre', 'apellido', 'rut', 'rol', 'is_staff', 'is_active')
    list_filter = ('rol', 'is_staff', 'is_active')
    search_fields = ('username', 'email', 'nombre', 'apellido', 'rut')
    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('nombre', 'apellido', 'rut', 'telefono', 'direccion', 'rol', 'fecha_registro', 'activo', 'avatar')}),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        (None, {'fields': ('nombre', 'apellido', 'rut', 'telefono', 'direccion', 'rol', 'activo', 'avatar')}),
    )
