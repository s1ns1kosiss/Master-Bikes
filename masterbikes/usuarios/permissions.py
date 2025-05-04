from django.contrib.auth.models import Permission
from django.contrib.contenttypes.models import ContentType
from django.db.models import Q
from django.db import transaction

def get_rol_permissions(rol):
    """
    Retorna los permisos específicos para cada rol
    """
    if rol == 'SUPERVISOR':
        # El supervisor tiene todos los permisos
        return Permission.objects.all()
    
    elif rol == 'VENDEDOR':
        # Permisos para vendedores
        return Permission.objects.filter(
            Q(content_type__app_label='productos') |
            Q(content_type__app_label='arriendos') |
            Q(content_type__app_label='promociones')
        )
    
    elif rol == 'TECNICO':
        # Permisos para técnicos
        return Permission.objects.filter(
            Q(content_type__app_label='reparaciones') |
            Q(content_type__app_label='productos')
        )
    
    elif rol == 'CLIENTE':
        # Permisos para clientes
        return Permission.objects.filter(
            Q(content_type__app_label='arriendos') |
            Q(content_type__app_label='reparaciones')
        )
    
    return Permission.objects.none()

def assign_rol_permissions(user):
    """
    Asigna los permisos correspondientes al rol del usuario
    """
    if not user.is_active:
        return

    with transaction.atomic():
        # Configurar permisos de staff y superusuario según el rol
        if user.rol == 'SUPERVISOR':
            user.is_staff = True
            user.is_superuser = True
        elif user.rol in ['VENDEDOR', 'TECNICO']:
            user.is_staff = True
            user.is_superuser = False
        else:
            user.is_staff = False
            user.is_superuser = False
        
        # Actualizar usuario sin llamar a save() personalizado
        type(user).objects.filter(pk=user.pk).update(
            is_staff=user.is_staff,
            is_superuser=user.is_superuser
        )
        
        # Limpiar permisos existentes
        user.user_permissions.clear()
        
        # Obtener y asignar nuevos permisos
        permissions = get_rol_permissions(user.rol)
        user.user_permissions.add(*permissions) 