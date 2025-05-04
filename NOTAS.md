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
### Sistema de Autenticación
- Implementado sistema completo de login y registro
- Templates creados para login y registro
- Configuración de URLs y vistas para autenticación
- Redirecciones configuradas en settings.py
- Implementación de mensajes de error y éxito

### Gestión de Usuarios
- Implementado sistema de permisos
- Creados templates específicos para clientes:
  - Perfil de cliente
  - Arriendos del cliente
  - Reparaciones del cliente
- Agregados comandos de gestión de usuarios para desarrollo
- Implementación de formularios de registro y edición
- Creación de vistas para perfil y edición de usuario

### Productos
- Templates creados:
  - Lista de productos
  - Detalle de producto
  - Formulario de producto
- Implementada lógica de visualización y gestión
- Integración con sistema de imágenes

### Arriendos
- Templates creados:
  - Lista de arriendos
  - Detalle de arriendo
  - Formulario de arriendo
- Formulario implementado con validaciones:
  - Validación de fechas
  - Filtrado de productos disponibles
- Lógica de negocio para arriendos
- Sistema de estados y seguimiento

### Reparaciones
- Templates creados:
  - Lista de reparaciones
  - Detalle de reparación
  - Formulario de reparación
- Formularios implementados:
  - Formulario para clientes
  - Formulario para staff con campos adicionales
- Lógica de negocio para reparaciones
- Sistema de asignación de técnicos

### Plantillas Base
- Actualizada la plantilla base con navegación
- Mejorada la página de inicio
- Implementado sistema de mensajes
- Integración de Bootstrap 5 y Font Awesome
- Diseño responsive

### URLs Disponibles
- http://127.0.0.1:8000/ - Página de inicio
- http://127.0.0.1:8000/usuarios/login/ - Iniciar sesión
- http://127.0.0.1:8000/usuarios/registro/ - Registrarse
- http://127.0.0.1:8000/productos/ - Lista de productos
- http://127.0.0.1:8000/arriendos/ - Lista de arriendos
- http://127.0.0.1:8000/reparaciones/ - Lista de reparaciones

## Configuración del Entorno
1. Clonar el repositorio
2. Crear entorno virtual: `python -m venv venv`
3. Activar entorno virtual:
   - Windows: `venv\Scripts\activate`
   - Linux/Mac: `source venv/bin/activate`
4. Instalar dependencias: `pip install -r requirements.txt`
5. Aplicar migraciones: `python manage.py migrate`
6. Crear superusuario: `python manage.py createsuperuser`
7. Crear usuarios de prueba: `python manage.py create_test_users`
8. Ejecutar servidor: `python manage.py runserver`

## Pendientes y Próximos Pasos
- Implementar sistema de promociones
- Desarrollar sistema de despachos
- Agregar reportes y estadísticas
- Mejorar la interfaz de usuario
- Implementar sistema de pagos
- Migrar a PostgreSQL en producción

## Tips para desarrollo colaborativo
- Subir cambios frecuentemente a la rama `dev`
- Usar mensajes de commit claros y siguiendo la convención
- Documentar decisiones importantes en este archivo
- Mantener actualizado el archivo NOTAS.md con los avances

---

*Actualizado: 19/03/2024 - Implementación de sistema de autenticación, gestión de usuarios, productos, arriendos y reparaciones*

# Notas de Desarrollo - MasterBikes

## Últimos Cambios Realizados

### Sistema de Autenticación
- Implementado sistema completo de login y registro
- Templates creados para login y registro
- Configuración de URLs y vistas para autenticación
- Redirecciones configuradas en settings.py

### Gestión de Usuarios
- Implementado sistema de permisos
- Creados templates específicos para clientes:
  - Perfil de cliente
  - Arriendos del cliente
  - Reparaciones del cliente
- Agregados comandos de gestión de usuarios para desarrollo

### Productos
- Templates creados:
  - Lista de productos
  - Detalle de producto
  - Formulario de producto
- Implementada lógica de visualización y gestión

### Arriendos
- Templates creados:
  - Lista de arriendos
  - Detalle de arriendo
  - Formulario de arriendo
- Formulario implementado con validaciones
- Lógica de negocio para arriendos

### Reparaciones
- Templates creados:
  - Lista de reparaciones
  - Detalle de reparación
  - Formulario de reparación
- Formularios implementados:
  - Formulario para clientes
  - Formulario para staff con campos adicionales
- Lógica de negocio para reparaciones

### Plantillas Base
- Actualizada la plantilla base con navegación
- Mejorada la página de inicio
- Implementado sistema de mensajes

### Mejoras visuales y refactor de estructura (Abril 2025)
- Unificación y modernización del footer y navbar en `base.html` para lograr una navegación y pie de página consistentes en todo el sitio.
- Eliminación de footers y navbars duplicados en las plantillas, asegurando limpieza y claridad en la estructura.
- Footer moderno, con enlaces sociales y tagline, presente en todas las páginas.
- Rediseño visual del hero en la página de inicio: altura y padding optimizados, degradado más suave, texto principal y subtítulo con tamaño equilibrado, y SVG decorativo mejor posicionado.
- Agregada flecha animada de scroll en el hero para invitar a explorar el contenido.
- Transición visual más fluida entre el hero y las tarjetas principales.
- Mejoras de responsividad y adaptación a dispositivos móviles en el hero y elementos principales.
- Separación de commits por tipo de cambio (estructura global vs. mejoras visuales) y mensajes de commit descriptivos para facilitar el seguimiento del historial.

## URLs Disponibles
- http://127.0.0.1:8000/ - Página de inicio
- http://127.0.0.1:8000/usuarios/login/ - Iniciar sesión
- http://127.0.0.1:8000/usuarios/registro/ - Registrarse
- http://127.0.0.1:8000/productos/ - Lista de productos
- http://127.0.0.1:8000/arriendos/ - Lista de arriendos
- http://127.0.0.1:8000/reparaciones/ - Lista de reparaciones

## Configuración del Entorno
1. Clonar el repositorio
2. Crear entorno virtual: `python -m venv venv`
3. Activar entorno virtual:
   - Windows: `venv\Scripts\activate`
   - Linux/Mac: `source venv/bin/activate`
4. Instalar dependencias: `pip install -r requirements.txt`
5. Aplicar migraciones: `python manage.py migrate`
6. Crear superusuario: `python manage.py createsuperuser`
7. Crear usuarios de prueba: `python manage.py create_test_users`
8. Ejecutar servidor: `python manage.py runserver`

## Próximos Pasos
- Implementar sistema de promociones
- Desarrollar sistema de despachos
- Agregar reportes y estadísticas
- Mejorar la interfaz de usuario
- Implementar sistema de pagos 