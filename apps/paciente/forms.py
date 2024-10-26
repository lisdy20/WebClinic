from apps.common import forms
from .models import (
    Paciente
    )

class PacienteForm(forms.GenericForm):
    class Meta:
        model = Paciente
        fields = ['nombre', 'apellido', 'dpi', 'nit', 'direccion', 'fechanac', 'genero', 'telefono']