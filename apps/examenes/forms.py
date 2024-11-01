from apps.common import forms
from .models import ExInterno,ExLaboratorio,DocResInterno,DocResLaboratorio

class ExamenInternoForm(forms.GenericForm):
    class Meta:
        model = ExInterno
        fields = ['detallecita', 'motivo', 'nombredoctor','activo']

class DocResInternoForm(forms.GenericForm):
    class Meta:
        model = DocResInterno
        fields = ['nombre', 'ubicacion', 'exinterno', 'activo']
        
class ExLaboratorioForm(forms.GenericForm):
    class Meta:
        model = ExLaboratorio
        fields = ['cita', 'motivo', 'nombrelab', 'activo']
        
class DocResLaboratorioForm(forms.GenericForm):
    class Meta:
        model = DocResLaboratorio
        fields = ['nombre', 'ubicacion', 'exlaboratorio', 'activo']