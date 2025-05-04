# MasterBikes

Plataforma web para gestión integral de arriendo, venta y reparación de bicicletas.

## Requisitos Previos

- Python 3.8 o superior
- pip (gestor de paquetes de Python)
- Git
- PostgreSQL (opcional, para producción)

## Instalación

1. **Clonar el repositorio**
   ```bash
   git clone https://github.com/s1ns1kosiss/Master-Bikes.git
   cd Master-Bikes
   ```

2. **Crear y activar entorno virtual**
   ```bash
   # Windows
   python -m venv venv
   venv\Scripts\activate

   # Linux/Mac
   python3 -m venv venv
   source venv/bin/activate
   ```
   > **Nota**: El entorno virtual debe estar activado para todos los comandos siguientes.

3. **Instalar dependencias**
   ```bash
   # Para desarrollo
   pip install -r requirements.txt

   # Para desarrollo con herramientas adicionales
   pip install -r requirements-dev.txt
   ```

4. **Configurar variables de entorno**
   ```bash
   # Copiar el archivo de ejemplo
   cp .env.example .env
   
   # Editar el archivo .env con tus configuraciones
   ```

5. **Configurar base de datos**
   - Para desarrollo (SQLite):
     - No se requiere configuración adicional
     - La base de datos se creará automáticamente

   - Para producción (PostgreSQL):
     - Instalar PostgreSQL
     - Crear base de datos
     - Configurar variables de entorno en .env
     - Actualizar settings.py si es necesario

6. **Aplicar migraciones**
   ```bash
   python manage.py migrate
   ```

7. **Crear superusuario**
   ```bash
   python manage.py createsuperuser
   ```
   > **Nota**: El superusuario es necesario para acceder al panel de administración.

8. **Iniciar servidor de desarrollo**
   ```bash
   python manage.py runserver
   ```

## Estructura del Proyecto

```
masterbikes/
├── usuarios/          # Gestión de usuarios y autenticación
├── productos/         # Catálogo de bicicletas y accesorios
├── arriendos/         # Gestión de arriendos
├── reparaciones/      # Servicio técnico
├── despachos/         # Gestión de entregas
├── promociones/       # Sistema de promociones
├── reportes/          # Generación de reportes
└── templates/         # Plantillas HTML
```

## Dependencias Principales

- Django 5.2
- Pillow (para manejo de imágenes)
- django-widget-tweaks (para formularios)
- psycopg2-binary (para PostgreSQL)
- python-dotenv (para variables de entorno)

## Desarrollo

1. **Crear una rama para desarrollo**
   ```bash
   git checkout -b dev
   ```

2. **Instalar dependencias de desarrollo**
   ```bash
   pip install -r requirements-dev.txt
   ```

3. **Ejecutar pruebas**
   ```bash
   python manage.py test
   ```

4. **Formatear código**
   ```bash
   # Formatear con black
   black .

   # Ordenar imports
   isort .

   # Verificar estilo
   flake8
   ```

## Despliegue

1. **Configurar variables de entorno**
   - Crear archivo .env con las configuraciones necesarias
   - No subir .env al repositorio
   - Usar .env.example como referencia

2. **Configurar base de datos PostgreSQL**
   - Crear base de datos
   - Configurar usuario y permisos
   - Actualizar variables de entorno

3. **Recolectar archivos estáticos**
   ```bash
   python manage.py collectstatic
   ```

## Contribución

1. Fork el repositorio
2. Crear una rama para tu feature (`git checkout -b feature/AmazingFeature`)
3. Commit tus cambios (`git commit -m 'Add some AmazingFeature'`)
4. Push a la rama (`git push origin feature/AmazingFeature`)
5. Abrir un Pull Request

## Notas Adicionales

- Revisar NOTAS.md para más detalles sobre el proyecto
- Seguir las convenciones de commit establecidas
- Mantener la documentación actualizada
- Asegurarse de que el entorno virtual esté activado
- No subir archivos sensibles al repositorio

## Soporte

Para soporte, contactar a [tu-email@ejemplo.com]

## Licencia

Este proyecto está bajo la Licencia MIT - ver el archivo [LICENSE.md](LICENSE.md) para más detalles. 