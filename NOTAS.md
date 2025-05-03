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

## Pendientes y Próximos Pasos
- Definir modelos para despachos, promociones y reportes
- Crear estructura de templates y archivos estáticos (Bootstrap, base.html)
- Implementar vistas, formularios y lógica de negocio para cada módulo
- Configurar control de acceso por roles

## Tips para desarrollo colaborativo
- Subir cambios frecuentemente a la rama `dev`
- Usar mensajes de commit claros y siguiendo la convención
- Documentar decisiones importantes en este archivo

---

*Actualiza este archivo cada vez que tomes una decisión importante o avances con una nueva funcionalidad.* 