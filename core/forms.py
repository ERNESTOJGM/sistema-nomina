from django import forms
from .models import Empleado

class EmpleadoForm(forms.ModelForm):
    class Meta:
        model = Empleado
        fields = ["cedula", "nombre", "fecha_ingreso", "sueldo_basico", "ayuda_ciudad"]
        widgets = {
            "fecha_ingreso": forms.DateInput(attrs={"type": "date"}),
            "sueldo_basico": forms.NumberInput(attrs={"step": "0.01", "min": "0"}),
            "ayuda_ciudad": forms.NumberInput(attrs={"step": "0.01", "min": "0"}),
        }