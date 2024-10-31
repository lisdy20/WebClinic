from apps.common import forms
from .models import (
    Paciente,
    Antecedente,
    )

class PacienteForm(forms.GenericForm):
    class Meta:
        model = Paciente
        fields = ['nombre', 'apellido', 'dpi', 'nit', 'direccion', 'fechanac', 'genero', 'telefono']

class AntecedenteForm(forms.GenericForm):
    class Meta:
        model = Antecedente
        fields = ['tipoantecedente', 'descripcion', 'paciente', 'activo']