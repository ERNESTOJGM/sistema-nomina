# Nomina PDVSA - Sistema de Gestion de Empleados

Aplicacion web desarrollada con Django 5.2 para la gestion de nomina
de empleados de PDVSA, siguiendo la metodologia de desarrollo en V.

## Necesidad profesional que resuelve

Un profesional de Recursos Humanos necesita una herramienta web para
registrar, consultar y gestionar datos de nomina de empleados,
calculando automaticamente quincenas, caja de ahorros, fideicomiso
y anios de servicio, con acceso diferenciado por roles.

## Metodologia de desarrollo en V - Fase descendente

### 1. Analisis de Requisitos
- Registro e inicio de sesion de usuarios.
- Roles: Administrador, Gestor, Usuario, Visitante.
- CRUD de empleados.
- Busqueda por nombre o cedula.
- Calculo automatico de quincenas y beneficios.

### 2. Analisis del Sistema
Arquitectura cliente-servidor con Django (MVT) y SQLite.
Autenticacion con roles diferenciados.

### 3. Diseno de Software / Arquitectura

| Capa | Tecnologia |
|---|---|
| Backend | Python 3.12 + Django 5.2 |
| Base de datos | SQLite |
| Frontend | Templates HTML/CSS |
| Versionado | Git + GitHub |

### 4. Diseno de Modulos
Modelo Empleado con campos de nomina y propiedades calculadas.
Roles como Group de Django. Signal post_save asigna rol Usuario.

### Punto de Inflexion - Codificacion
A partir de aqui empieza la fase ascendente.

## Fase ascendente (construccion)

### Instalacion

    python -m venv env
    env\Scripts\activate
    pip install -r requirements.txt

### Configuracion
Copia .env.example a .env y genera una SECRET_KEY:

    python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"

### Ejecucion

    python manage.py migrate
    python manage.py init_roles
    python manage.py createsuperuser
    python manage.py runserver

Acceso: http://127.0.0.1:8000

## Roles y permisos

| Rol | Ver | Detalle | Crear | Editar | Eliminar | Admin |
|---|---|---|---|---|---|---|
| Visitante | No | No | No | No | No | No |
| Usuario | Si | Si | No | No | No | No |
| Gestor | Si | Si | Si | Si | Si | No |
| Administrador | Si | Si | Si | Si | Si | Si |

## Nota sobre el entorno

Por politicas de TI de la empresa (equipo corporativo sin permisos de
administrador local), no fue posible habilitar la caracteristica
Virtual Machine Platform requerida por Docker Desktop. La app fue
desarrollada y probada con entorno virtual de Python (venv).

## Alcance del Modulo I

- Stack Django (archivos Docker incluidos)
- Repositorio GitHub
- Backend en 2 apps (users, core)
- Registro, login, logout
- 4 roles con templates diferenciados
- Django Admin configurado
- CRUD de empleados con calculos automaticos
- README con metodologia en V