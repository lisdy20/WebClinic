from django.shortcuts import render
from django.urls import reverse_lazy
from apps.common import utils,views
from rest_framework.reverse import reverse
from . import models,admin,forms,serializers

# Create your views here.
class ListaCitaTemplateView(views.GenericTemplateView):
    template_name = 'lista_citas.html'

    def get(self, request):
        url = reverse('citas-list',request=request)
        data = self.get_paginator(request=request,model=models.Cita)
        campos = admin.CitaAdmin.list_display
        campos = utils.format_names(names=campos)
        data['campos']=campos
        data['url']=url
        return render(request=request, template_name=self.template_name,context=data)
    

class ListaServicioTemplateView(views.GenericTemplateView):
    template_name = 'lista_servicios.html'

    def get(self, request):
        url = reverse('servicios-list',request=request)
        url_edit = reverse_lazy('editar-servicio',kwargs={'pk':0})
        print(url_edit)
        data = self.get_paginator(request=request,model=models.Servicio)
        campos = admin.ServicioAdmin.list_display
        campos = utils.format_names(names=campos)
        data['campos']=campos
        data['url']=url
        data['url_edit']=str(url_edit).replace('0/','')
        return render(request=request, template_name=self.template_name,context=data)
    

# - - - - - - - - - - - - - - - - - - - - - -

class ServicioCreateView(views.GenericTemplateView):
    template_name='agregar_servicio.html'

    def get(self, request, *args, **kwargs):
        data={}
        data['form']=forms.ServicioForm
        url = reverse('servicios-list',request=request)
        data['url'] = url
        return render(request=request,template_name=self.template_name,context=data)
    
class ServicioEditView(views.GenericTemplateView):
    template_name = 'editar_servicio.html'
    
    def get(self, request, *args, **kwargs):
        # Obtener el producto por su 'pk'
        data={}
        entity = utils.model_or_none(model=models.Servicio, pk=kwargs['pk'])
        form = forms.ServicioForm(instance=entity)  # Pasa la instancia del modelo existente al formulario
        url = reverse('servicios-list',request=request)
        data['url'] = url
        data['form']=form
        data['entity']=entity
        return render(request=request, template_name=self.template_name,context=data)

class CitaCreateView(views.GenericTemplateView):
    template_name='agregar_cita.html'

    def get(self, request, *args, **kwargs):
        data={}
        data['form']=forms.CitaForm
        url = reverse('citas-list',request=request)
        data['url'] = url
        return render(request=request,template_name=self.template_name,context=data)
    
    
# ---------------------------------------------------------------- DRF Views
class ServicioViewSet(views.GenericViewSet):
    queryset = models.Servicio.objects.all()
    serializer_class = serializers.ServicioSerializer

class CitaViewSet(views.GenericViewSet):
    queryset = models.Cita.objects.all()
    serializer_class = serializers.CitaSerializer