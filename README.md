# Sistema de Gestión de Cálculo de Beneficios Empleados Petroleros

Aplicación web desarrollada con Django 5.2 para la gestión de nómina
de empleados petroleros, siguiendo la metodología de desarrollo en V.

## Necesidad profesional que resuelve

Un profesional de Recursos Humanos necesita una herramienta web para
registrar, consultar y gestionar datos de nómina de empleados,
calculando automáticamente quincenas, caja de ahorros, fideicomiso
y años de servicio, con acceso diferenciado por roles.

## Metodología de desarrollo en V - Fase descendente

### 1. Análisis de Requisitos
- Registro e inicio de sesión de usuarios.
- Roles: Administrador, Gestor, Usuario, Visitante.
- CRUD de empleados.
- Búsqueda por nombre o cédula.
- Cálculo automático de quincenas y beneficios.

### 2. Análisis del Sistema
Arquitectura cliente-servidor con Django (MVT) y SQLite.
Autenticación con roles diferenciados.

### 3. Diseño de Software / Arquitectura

| Capa | Tecnología |
|---|---|
| Backend | Python 3.12 + Django 5.2 |
| Base de datos | SQLite |
| Frontend | Templates HTML/CSS |
| Versionado | Git + GitHub |

### 4. Diseño de Módulos
Modelo Empleado con campos de nómina y propiedades calculadas.
Roles como Group de Django. Signal post_save asigna rol Usuario.

### Punto de Inflexión - Codificación
A partir de aquí empieza la fase ascendente.

## Fase ascendente (construcción)

### Instalación

    python -m venv env
    env\Scripts\activate
    pip install -r requirements.txt

### Configuración
Copia .env.example a .env y genera una SECRET_KEY:

    python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"

### Ejecución

    python manage.py migrate
    python manage.py init_roles
    python manage.py createsuperuser
    python manage.py runserver

Acceso: http://127.0.0.1:8000

## Roles y permisos

| Rol | Ver | Detalle | Crear | Editar | Eliminar | Admin |
|---|---|---|---|---|---|---|
| Visitante | No | No | No | No | No | No |
| Usuario | Sí | Sí | No | No | No | No |
| Gestor | Sí | Sí | Sí | Sí | Sí | No |
| Administrador | Sí | Sí | Sí | Sí | Sí | Sí |

## Nota sobre el entorno

Por políticas de TI de la empresa (equipo corporativo sin permisos de
administrador local), no fue posible habilitar la característica
Virtual Machine Platform requerida por Docker Desktop. La app fue
desarrollada y probada con entorno virtual de Python (venv).

## Alcance del Módulo I

- Stack Django (archivos Docker incluidos)
- Repositorio GitHub
- Backend en 2 apps (users, core)
- Registro, login, logout
- 4 roles con templates diferenciados
- Django Admin configurado
- CRUD de empleados con cálculos automáticos
- README con metodología en V