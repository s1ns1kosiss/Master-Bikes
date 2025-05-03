# NOTAS DEL PROYECTO MASTERBIKES

## Resumen del Proyecto
Plataforma web para gestión integral de arriendo, venta y reparación de bicicletas.

## Estructura de Apps
- usuarios: Modelo de usuario personalizado con roles (Cliente, Técnico, Vendedor, Supervisor)
- productos: Modelo único para bicicletas y accesorios
- arriendos: Gestión de solicitudes y control de arriendos
- reparaciones: Solicitud y seguimiento de servicios técnicos
- despachos: (pendiente)
- promociones: (pendiente)
- reportes: (pendiente)

## Convención de Commits
- `feature:` para lógica, modelos y funcionalidades principales
- `design:` para cambios de estructura, admin, documentación, etc.

## Decisiones y Modelos Clave
### Usuario Personalizado
- Hereda de AbstractUser
- Campos: nombre, apellido, rut, teléfono, dirección, rol, fecha_registro, activo, avatar
- Roles: Cliente, Técnico, Vendedor, Supervisor

### Producto
- Modelo único con campo `tipo` (bicicleta/accesorio)
- Campos: nombre, descripcion, precio, stock, tipo, marca, modelo, rodado, color, año, tipo_accesorio, imagen, fecha_creacion

### Arriendo
- usuario, producto, fecha_inicio, fecha_fin, estado, total, fecha_solicitud, observaciones, entregado, fecha_entrega, fecha_devolucion_real, metodo_pago, descuento_aplicado

### Reparacion
- usuario, producto, tecnico, descripcion_problema, estado, fecha_solicitud, fecha_inicio, fecha_fin, costo, observaciones

## Avances Realizados
### Estructura Base y Templates
- Implementación de base.html con navbar responsive y footer
- Creación de home.html con secciones principales
- Configuración de vistas y URLs principales
- Integración de Bootstrap 5 y Font Awesome

### Sistema de Usuarios
- Implementación de formularios de registro y edición
- Creación de vistas para perfil y edición de usuario
- Configuración de URLs para gestión de usuarios
- Integración de django-widget-tweaks para mejor presentación de formularios

### Configuración del Proyecto
- Actualización de settings.py con apps y configuraciones
- Configuración de URLs principales
- Actualización de requirements.txt con nuevas dependencias
- Configuración de archivos estáticos y media

## Pendientes y Próximos Pasos
- Implementar vistas y formularios para productos
- Desarrollar sistema de arriendos
- Crear sistema de reparaciones
- Configurar autenticación y permisos por roles
- Implementar sistema de despachos
- Desarrollar sistema de promociones
- Crear módulo de reportes

## Tips para desarrollo colaborativo
- Subir cambios frecuentemente a la rama `dev`
- Usar mensajes de commit claros y siguiendo la convención
- Documentar decisiones importantes en este archivo

---

*Actualizado: [Fecha actual] - Implementación de sistema de usuarios y estructura base* 