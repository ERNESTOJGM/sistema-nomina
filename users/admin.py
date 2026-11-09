"""
Archivo de configuración del panel de administración de Django admin.py.
Personaliza la vista del modelo de usuario predeterminado User para 
mostrar columnas específicas y agregar filtros adicionales en la interfaz de administración.
"""

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User


class CustomUserAdmin(BaseUserAdmin):
    """
    Clase personalizada para administrar el modelo User en el Django Administrador y 
    Hereda de la clase original UserAdmin para conservar
    todas sus funcionalidades base, permitiendo sobrescribir comportamientos específicos.
    """
    
    # Define las columnas que se mostrarán en la tabla de la lista de usuarios dentro del panel de administración.
    list_display = ("username", "email", "is_staff", "is_superuser")
    
    # Amplía los filtros laterales predeterminados sumando la opción de filtrar por grupos de usuarios ("groups").
    list_filter = BaseUserAdmin.list_filter + ("groups",)


# Django registra el modelo User de forma nativa con su configuración estándar.
# Por lo tanto, es necesario desregistrarlo primero antes de asociar una configuración personalizada.
admin.site.unregister(User)

# Registra nuevamente el modelo User en el panel de administración utilizando la clase personalizada `CustomUserAdmin`.
admin.site.register(User, CustomUserAdmin)