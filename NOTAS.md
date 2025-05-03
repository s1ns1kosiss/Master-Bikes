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
- Cambio temporal a SQLite para desarrollo local

### Migraciones y Modelos
- Creación de migraciones iniciales para todas las apps
- Implementación de modelos para Usuario, Producto, Arriendo y Reparación
- Configuración de relaciones entre modelos
- Registro de modelos en el admin de Django

### URLs y Vistas
- Configuración de URLs para arriendos, productos y reparaciones
- Implementación de vistas básicas para cada módulo
- Estructuración de rutas siguiendo las mejores prácticas

## Pendientes y Próximos Pasos
- Implementar formularios para productos
- Desarrollar lógica de negocio para arriendos
- Crear sistema de seguimiento de reparaciones
- Configurar permisos específicos por roles
- Implementar sistema de despachos
- Desarrollar sistema de promociones
- Crear módulo de reportes
- Migrar a PostgreSQL en producción

## Plan de Trabajo en Computador de Casa
### Configuración de PostgreSQL
1. Clonar repositorio
2. Instalar dependencias del proyecto
3. Configurar PostgreSQL:
   - Crear base de datos
   - Configurar usuario y permisos
   - Actualizar settings.py con credenciales de PostgreSQL
4. Migrar datos de SQLite a PostgreSQL:
   - Crear script de migración
   - Verificar integridad de datos
   - Probar funcionalidades con nueva base de datos

### Desarrollo con PostgreSQL
1. Implementar formularios para productos
2. Desarrollar lógica de negocio para arriendos
3. Crear sistema de seguimiento de reparaciones
4. Configurar permisos específicos por roles
5. Implementar sistema de despachos
6. Desarrollar sistema de promociones
7. Crear módulo de reportes

### Pruebas y Optimización
1. Realizar pruebas de rendimiento
2. Optimizar consultas a la base de datos
3. Implementar índices necesarios
4. Configurar respaldos automáticos
5. Documentar procedimientos de mantenimiento

## Tips para desarrollo colaborativo
- Subir cambios frecuentemente a la rama `dev`
- Usar mensajes de commit claros y siguiendo la convención
- Documentar decisiones importantes en este archivo
- Mantener actualizado el archivo NOTAS.md con los avances

---

*Actualizado: 19/03/2024 - Implementación de migraciones y configuración de URLs y vistas* 