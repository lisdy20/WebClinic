from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from apps.common import utils,views
from rest_framework.reverse import reverse
from rest_framework import generics, viewsets
from . import models,admin,forms,serializers

# Create your views here.
class ListaCitaTemplateView(views.GenericTemplateView):
    template_name = 'lista_citas.html'

    def get(self, request):
        page_obj = self.get_paginator(request=request,model=models.Cita)
        campos = admin.CitaAdmin.list_display
        campos = utils.format_names(names=campos)
        data={'page_obj': page_obj,'campos':campos}
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

class ServicioCreateView(CreateView):
    model = models.Servicio
    form_class = forms.ServicioForm
    template_name='agregar_servicio.html'
    success_url = reverse_lazy('lista-servicios')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        url = reverse('servicios-list',request=self.request)
        # Pasar el mensaje al contexto si existe en la sesión
    
        context['url'] = url
    
        return context
    
class ServicioViewSet(viewsets.ModelViewSet):
    queryset = models.Servicio.objects.all()
    serializer_class = serializers.ServicioSerializer