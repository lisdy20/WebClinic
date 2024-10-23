from django.http.response import HttpResponse as HttpResponse
from django.shortcuts import render
from apps.common import utils,views
from rest_framework.reverse import reverse
from rest_framework import viewsets
from . import models,admin,forms,serializers

# Create your views here.
class ListaCitaTemplateView(views.GenericTemplateView):
    template_name = 'lista_citas.html'

    def get(self, request):
        url = reverse('citas-list',request=request)
        page_obj = self.get_paginator(request=request,model=models.Cita)
        campos = admin.CitaAdmin.list_display
        campos = utils.format_names(names=campos)
        data={'page_obj': page_obj,'campos':campos,'url':url}
        return render(request=request, template_name=self.template_name,context=data)
    

class ListaServicioTemplateView(views.GenericTemplateView):
    template_name = 'lista_servicios.html'

    def get(self, request):
        url = reverse('servicios-list',request=request)
        page_obj = self.get_paginator(request=request,model=models.Servicio)
        campos = admin.ServicioAdmin.list_display
        campos = utils.format_names(names=campos)
        data={'page_obj': page_obj,'campos':campos,'url':url}
        return render(request=request, template_name=self.template_name,context=data)
    

# - - - - - - - - - - - - - - - - - - - - - -

class ServicioCreateView(views.GenericTemplateView):
    template_name='agregar_servicio.html'

    def get(self, request, *args, **kwargs):
        data={}
        data['form']=forms.ServicioForm
        url = reverse('servicios-list',request=request)
        # Pasar el mensaje al contexto si existe en la sesión
        data['url'] = url
        return render(request=request,template_name=self.template_name,context=data)
    
class CitaCreateView(views.GenericTemplateView):
    template_name='agregar_cita.html'

    def get(self, request, *args, **kwargs):
        data={}
        data['form']=forms.CitaForm
        url = reverse('citas-list',request=request)
        # Pasar el mensaje al contexto si existe en la sesión
        data['url'] = url
        return render(request=request,template_name=self.template_name,context=data)
    
# ---------------------------------------------------------------- DRF Views
class ServicioViewSet(viewsets.ModelViewSet):
    queryset = models.Servicio.objects.all()
    serializer_class = serializers.ServicioSerializer

class CitaViewSet(viewsets.ModelViewSet):
    queryset = models.Cita.objects.all()
    serializer_class = serializers.CitaSerializer