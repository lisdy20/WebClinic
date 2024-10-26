from apps.common import forms
from .models import Medicamento

class MedicamentoForm(forms.GenericForm):
    class Meta:
        model = Medicamento
        fields = ['medicamento', 'descripcion']
        