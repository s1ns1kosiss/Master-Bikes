# MasterBikes

Plataforma web para gestión integral de arriendo, venta y reparación de bicicletas.

## Requisitos

- Python 3.10+
- (Opcional) PostgreSQL para producción
- pip

## Instalación

1. Clona el repositorio:
   ```bash
   git clone https://github.com/s1ns1kosiss/Master-Bikes.git
   cd Master-Bikes
   ```

2. Crea y activa un entorno virtual:
   - En Windows:
     ```bash
     python -m venv venv
     venv\Scripts\activate
     ```
   - En Mac/Linux:
     ```bash
     python3 -m venv venv
     source venv/bin/activate
     ```

3. Instala las dependencias:
   ```bash
   pip install -r requirements.txt
   ```

4. (Opcional) Configura la base de datos en `settings.py` si usarás PostgreSQL.

5. Aplica migraciones:
   ```bash
   python manage.py migrate
   ```

6. Ejecuta el servidor de desarrollo:
   ```bash
   python manage.py runserver
   ```

---

## Estructura del Proyecto

- `usuarios/` - Gestión de usuarios y roles
- `productos/` - Catálogo de bicicletas y accesorios
- `arriendos/` - Gestión de arriendos
- `reparaciones/` - Servicios técnicos
- `despachos/` - Entregas y despachos
- `promociones/` - Campañas y correos
- `reportes/` - Visualización de datos

---

## Notas

- Por defecto, la base de datos está configurada para PostgreSQL. Si no tienes PostgreSQL, puedes cambiar a SQLite en `settings.py` para desarrollo local.
- Recuerda crear un superusuario para acceder al panel de administración:
  ```bash
  python manage.py createsuperuser
  ``` 