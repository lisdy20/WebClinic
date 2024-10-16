from django.shortcuts import render
from django.views.generic import TemplateView
from django.conf import settings

from apps.clinica import models as modelsClinica
from apps.usuarios import models as modelsUsuario

# Create your views here.
class InicioTemplateView(TemplateView):
    template_name = 'inicio/index.html'

    def get(self, request):
        data={}
        inicio=True
        servicios = modelsClinica.Servicio.objects.all()
        hay_servicios=len(servicios)>0

        empleados = modelsUsuario.Perfil.objects.all()
        hay_empleados=len(empleados)>0

        data['hay_servicios'] = hay_servicios
        data['servicios'] = servicios

        data['hay_empleados']=hay_empleados
        data['empleados'] = empleados

        data['inicio']=inicio
        return render(request=request, template_name=self.template_name,context=data)
    
class ServiciosTemplateView(TemplateView):
    template_name = 'inicio/servicios.html'

    def get(self, request):
        return render(request=request,template_name=self.template_name)
    
class NuestroEquipoTemplateView(TemplateView):
    template_name = 'inicio/nuestro_equipo.html'

    def get(self, request):
        return render(request=request,template_name=self.template_name)

class ContactoTemplateView(TemplateView):
    template_name = 'inicio/contacto.html'

    def get(self, request):
        return render(request=request,template_name=self.template_name)
    
class PanelTemplateView(TemplateView):
    template_name = 'panel.html'

    def get(self, request):
        installed_apps = settings.INSTALLED_APPS
        modules=[app.split('.')[-1] for app in installed_apps if not app.startswith('django.')]
        data={'modules': modules}
        return render(request=request,template_name=self.template_name,context=data)