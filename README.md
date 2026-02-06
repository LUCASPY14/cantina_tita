# Cantina Tita - Sistema de Gestión

Sistema completo de gestión para Cantina Tita con backend API REST y frontend web.

## 🏗️ Arquitectura del Proyecto

El proyecto está dividido en tres servicios principales:

- **Backend**: API REST con Django + Django REST Framework
- **Frontend**: Aplicación web con Django + Tailwind CSS
- **MySQL**: Base de datos relacional

## 📁 Estructura del Proyecto

```
cantina_tita/
├── backend/              # API Backend (Django REST Framework)
│   ├── apps/
│   │   ├── inventario/  # App de gestión de inventario
│   │   ├── usuarios_portal/  # App de usuarios
│   │   └── ventas/      # App de ventas
│   ├── core/            # Configuración principal de Django
│   ├── Dockerfile
│   └── requirements.txt
├── frontend/            # Frontend Web (Django + Tailwind)
│   ├── apps/
│   │   └── web/        # App web principal
│   ├── frontend/       # Configuración de Django
│   ├── templates/      # Plantillas HTML
│   ├── static/         # Archivos estáticos
│   ├── Dockerfile
│   └── requirements.txt
├── docker-compose.yml   # Configuración de servicios Docker
└── README.md
```

## 🚀 Inicio Rápido

### Prerrequisitos

- Docker
- Docker Compose

### Levantar el Proyecto

```bash
# Construir y levantar todos los servicios
docker-compose up --build

# O en modo detached (segundo plano)
docker-compose up --build -d
```

### Acceder a los Servicios

- **Frontend**: http://localhost:3000
- **Backend API**: http://localhost:8000
- **Admin Django (Backend)**: http://localhost:8000/admin/
- **MySQL**: localhost:3307

### Credenciales de Acceso

**Admin del Backend:**
- Usuario: `admin`
- Email: `admin@cantina.com`
- Contraseña: `admin123`

**MySQL:**
- Base de datos: `cantina_tita_db`
- Usuario: `cantina_user`
- Contraseña: `cantina_password`
- Puerto: 3307

## 🔧 Comandos Útiles

### Gestión de Contenedores

```bash
# Ver estado de los contenedores
docker-compose ps

# Ver logs de todos los servicios
docker-compose logs

# Ver logs de un servicio específico
docker-compose logs backend
docker-compose logs frontend
docker-compose logs mysql

# Detener todos los servicios
docker-compose down

# Reiniciar un servicio específico
docker-compose restart backend
```

### Backend - Comandos Django

```bash
# Ejecutar migraciones
docker-compose exec backend python manage.py migrate

# Crear migraciones
docker-compose exec backend python manage.py makemigrations

# Crear superusuario
docker-compose exec backend python manage.py createsuperuser

# Acceder al shell de Django
docker-compose exec backend python manage.py shell

# Acceder a la terminal del contenedor
docker-compose exec backend bash
```

### Frontend - Comandos Django

```bash
# Ejecutar migraciones
docker-compose exec frontend python manage.py migrate

# Crear superusuario
docker-compose exec frontend python manage.py createsuperuser

# Acceder al shell de Django
docker-compose exec frontend python manage.py shell

# Acceder a la terminal del contenedor
docker-compose exec frontend bash
```

### Base de Datos

```bash
# Acceder a MySQL
docker-compose exec mysql mysql -u cantina_user -p cantina_tita_db
# Contraseña: cantina_password

# Backup de la base de datos
docker-compose exec mysql mysqldump -u cantina_user -p cantina_tita_db > backup.sql
```

## 🛠️ Desarrollo

### Agregar una Nueva App al Backend

```bash
# Crear la app dentro del contenedor
docker-compose exec backend python manage.py startapp nombre_app apps/nombre_app

# Agregar la app a INSTALLED_APPS en backend/core/settings.py
# 'apps.nombre_app',

# Crear modelos, vistas, serializadores, etc.
# Crear y ejecutar migraciones
docker-compose exec backend python manage.py makemigrations
docker-compose exec backend python manage.py migrate
```

### Instalar Dependencias

Si agregas nuevas dependencias en `requirements.txt`:

```bash
# Reconstruir el contenedor
docker-compose up --build backend
# o
docker-compose up --build frontend
```

## 📊 Estado Actual del Proyecto

### ✅ Completado

- ✅ Configuración de Docker Compose
- ✅ Backend API con Django REST Framework
- ✅ Frontend con Django
- ✅ Base de datos MySQL configurada
- ✅ Apps del backend creadas (inventario, usuarios_portal, ventas)
- ✅ Estructura base del proyecto
- ✅ CORS configurado para comunicación entre servicios

### 🔄 En Desarrollo

- 🔄 Modelos de datos para inventario
- 🔄 Endpoints de API REST
- 🔄 Interfaz de usuario del frontend
- 🔄 Autenticación y autorización

## 📝 Notas Importantes

1. El backend corre en el puerto **8000**
2. El frontend corre en el puerto **3000**
3. MySQL está expuesto en el puerto **3307** (para evitar conflictos con MySQL local)
4. Los cambios en el código se reflejan automáticamente gracias a los volúmenes montados
5. El frontend consume la API del backend en `http://backend:8000`

## 🤝 Contribuir

Para contribuir al proyecto:

1. Crear una rama para tu feature
2. Realizar los cambios
3. Asegurarte de que todo funcione con `docker-compose up --build`
4. Crear un pull request

## 📄 Licencia

Este proyecto es privado y confidencial.
