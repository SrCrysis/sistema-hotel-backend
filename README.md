# Sistema de Hotel - Backend

Proyecto backend desarrollado en Python + Django para la gestión de un sistema de hotel.

- **Evaluación 1:** base técnica del proyecto (repositorio, ambiente virtual y núcleo Django).
- **Evaluación 2:** modelo de datos con MariaDB, API REST con Django REST Framework y CRUD completo.

Desarrollado y probado con Python 3.14, Django 6.1 y MariaDB.

## Requisitos previos

- Python 3 y `pip`
- MariaDB (servidor en ejecución)
- Librerías del sistema para compilar `mysqlclient`:

Fedora / Nobara:

```bash
sudo dnf install mariadb-server mariadb-devel gcc python3-devel pkgconf-pkg-config
sudo systemctl enable --now mariadb
```

Debian / Ubuntu:

```bash
sudo apt install mariadb-server libmariadb-dev build-essential python3-dev pkg-config
```

## Instalación y ejecución

1. Clonar el repositorio:

```bash
   git clone <URL-del-repositorio>
   cd sistema-hotel-backend
```

2. Crear la base de datos, el usuario y sus permisos con el script SQL incluido:

```bash
   mysql -u root -p < sql/crear_db.sql
```

3. Crear el ambiente virtual y activarlo:

```bash
   python3 -m venv .venv
   source .venv/bin/activate
```

4. Instalar dependencias:

```bash
   pip install -r requirements.txt
```

5. Crear el archivo `.env` en la raíz del proyecto (junto a `manage.py`). Este archivo no se sube a git:

```
   SECRET_KEY=<clave-secreta>
   DEBUG=True
   DB_NAME=sistema_hotel
   DB_USER=sistema_hotel_user
   DB_PASSWORD=<contraseña-definida-en-crear_db.sql>
   DB_HOST=localhost
   DB_PORT=3306
```

   Para generar una `SECRET_KEY`:

```bash
   python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"
```

6. Aplicar las migraciones:

```bash
   python manage.py migrate
```

7. Ejecutar el servidor:

```bash
   python manage.py runserver
```

8. Abrir `http://127.0.0.1:8000/` (bienvenida) o `http://127.0.0.1:8000/api/` (API).

## Endpoints de la API

| Recurso | Lista y creación (GET, POST) | Detalle (GET, PUT, PATCH, DELETE) |
|---|---|---|
| Huéspedes | `/api/huespedes/` | `/api/huespedes/<id>/` |
| Habitaciones | `/api/habitaciones/` | `/api/habitaciones/<id>/` |
| Reservas | `/api/reservas/` | `/api/reservas/<id>/` |

En `Reserva`, los campos `habitacion` y `huesped` se envían como el `id` del registro relacionado, y las fechas en formato `AAAA-MM-DD`.