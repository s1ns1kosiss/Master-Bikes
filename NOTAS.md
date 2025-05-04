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

### Mejoras visuales y de experiencia en el registro de usuarios (junio 2025)
- Rediseño completo del formulario de registro para mayor claridad, orden y atractivo visual.
- Agrupación de campos en secciones: Datos personales, Datos de acceso y Seguridad, cada una con subtítulo e icono.
- Separadores visuales claros entre bloques para mejorar la jerarquía y la experiencia de usuario.
- Inputs con icono a la izquierda, labels arriba y feedback de error accesible.
- Medidor de fortaleza de contraseña y requisitos visuales alineados bajo el campo correspondiente.
- Botón de registro destacado y microinteracciones en inputs y botones.
- Responsive optimizado y accesibilidad mejorada (`aria-live` en feedback, navegación por teclado).
- Código y estilos limpios, listos para futuras mejoras.

#### Para continuar el desarrollo en otro equipo/PC:
1. Haz pull de la rama `dev` para obtener los últimos cambios.
2. Revisa el archivo `masterbikes/templates/usuarios/registro.html` para ver el nuevo diseño y estructura.
3. Si necesitas modificar estilos, están embebidos en el bloque `{% block extra_css %}` del template.
4. Prueba el registro en desktop y móvil para verificar la experiencia visual y de usuario.
5. Si quieres personalizar colores, iconos o subtítulos de sección, edita el bloque de estilos y los títulos en el template.
6. Mantén este archivo `NOTAS.md` actualizado con cualquier mejora o ajuste adicional.

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