from datetime import date
from decimal import Decimal
from django.conf import settings
from django.db import models

class Empleado(models.Model):
    usuario = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="empleados")
    cedula = models.CharField("Cedula", max_length=20, unique=True)
    nombre = models.CharField("Nombre y apellido", max_length=200)
    fecha_ingreso = models.DateField("Fecha de ingreso")
    sueldo_basico = models.DecimalField("Sueldo basico (USD)", max_digits=12, decimal_places=2)
    ayuda_ciudad = models.DecimalField("Ayuda de ciudad (USD)", max_digits=12, decimal_places=2, default=0)
    creado = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Empleado"
        verbose_name_plural = "Empleados"
        ordering = ["nombre"]

    def __str__(self):
        return f"{self.cedula} - {self.nombre}"

    @property
    def anios_servicio(self):
        hoy = date.today()
        fi = self.fecha_ingreso
        return hoy.year - fi.year - ((hoy.month, hoy.day) < (fi.month, fi.day))

    @property
    def primera_quincena(self):
        return (self.sueldo_basico + self.ayuda_ciudad) * Decimal("0.40")

    @property
    def quincena_30(self):
        return (self.sueldo_basico + self.ayuda_ciudad) * Decimal("0.60")

    @property
    def caja_ahorros(self):
        return (self.sueldo_basico * Decimal("15.5") / Decimal("100")) * Decimal("2")

    @property
    def fideicomiso(self):
        return self.sueldo_basico * Decimal("0.22") * Decimal("1.33")