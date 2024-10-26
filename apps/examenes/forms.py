from apps.common import forms
from .models import ExInterno

class ExamenInternoForm(forms.GenericForm):
    class Meta:
        model = ExInterno
        fields = ['detallecita', 'motivo', 'nombredoctor']
        
class ExamenExternoForm(forms.GenericForm):
    class Meta:
        model = ExInterno
        fields = ['detallecita', 'motivo', 'nombredoctor']
        