from django.contrib import admin
from .models import Empleado

@admin.register(Empleado)
class EmpleadoAdmin(admin.ModelAdmin):
    list_display = ("cedula", "nombre", "fecha_ingreso", "sueldo_basico", "anios_servicio")
    search_fields = ("cedula", "nombre")
    list_filter = ("fecha_ingreso",)

    @admin.display(description="Anios servicio")
    def anios_servicio(self, obj):
        return obj.anios_servicio