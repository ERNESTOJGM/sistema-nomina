"""
Archivo principal de enrutamiento a la URL (urls.py) del proyecto Django.
Este archivo define la estructura de rutas globales de la aplicación 
y personaliza los títulos del panel de administración.
"""

from django.contrib import admin
from django.urls import include, path

# --- Personalización del Panel de Administración ---
# Texto que aparece en la parte superior encabezado de cada página del panel de administración.
admin.site.site_header = "Nómina Trabajador"

# Texto que aparece en la pestaña - título de la ventana del navegador.
admin.site.site_title = "Nómina Trabajador"

# Encabezado principal que se muestra en la página de inicio del panel de administración.
admin.site.index_title = "Panel de Administración"


# --- Estructura de Rutas de la Aplicación ---
urlpatterns = [
    # Ruta para acceder al panel de administración de Django.
    path("admin/", admin.site.urls),
    
    # Incluye las rutas del módulo 'users' para la gestión interna de usuarios.
    path("users/", include("users.urls")),
    
    # Incluye las rutas del módulo 'core' para la gestión de nómina.
    path("nomina/", include("core.urls")),
    
    # Ruta raíz de la aplicación.
    # Incluye las rutas públicas accesibles sin autenticación o de vista general desde 'users.urls_public'
    path("", include("users.urls_public")),
]