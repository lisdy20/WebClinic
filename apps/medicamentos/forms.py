from apps.common import forms
from .models import Medicamento,RecetaMedica,DetalleRecetaMe

class MedicamentoForm(forms.GenericForm):
    class Meta:
        model = Medicamento
        fields = ['medicamento', 'descripcion']

class RecetaMedicaForm(forms.GenericForm):
    class Meta:
        model = RecetaMedica
        fields = ['fecha', 'doctor','observaciones']

class DetalleRecetaForm(forms.GenericForm):
    class Meta:
        model = DetalleRecetaMe
        fields = ['recetamedica','medicamento','dosiscantidad','dosistiempo']
        