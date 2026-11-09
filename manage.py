"""
Utilidad de línea de comandos estándar de Django para tareas administrativas.
Sirve como el punto de entrada principal para interactuar 
con el proyecto Django desde la terminal en este caso, configurado bajo el proyecto 'Calculo_Prestaciones_Trabajador'.
"""
import os
import sys


def main():
    """
    Función principal que configura el entorno y ejecuta las tareas administrativas
    solicitadas a través de la línea de comandos. Establece la variable de entorno predeterminada que le indica a Django
    qué archivo de configuración debe utilizar.
    """
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'prestaciones.settings')
    
    try:
        # Intenta importar la utilidad central de Django encargada de procesar 
        # los comandos de la consola como runserver, makemigrations, migrate.
        
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        
        # Si la importación falla, significa que Django no está instalado o 
        # que el entorno virtual no ha sido activado correctamente. Se lanza 
        # una excepción con un mensaje guía para solucionar el problema.
        
        raise ImportError(
            "No se pudo importar Django. ¿Estás seguro de que está instalado y "
            "disponible en tu variable de entorno PYTHONPATH? ¿Olvidaste "
            "activar un entorno virtual?"
        ) from exc
        
    # Pasa los argumentos de la línea de comandos a la función de Django
    # para que procese la orden correspondiente como por ejemplo el código: manage.py y runserver.
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    # Evalúa si el script se está ejecutando directamente desde la terminal.
    # Si es así, se invoca la función principal main().
    main()