from django.shortcuts import render
from django.urls import reverse_lazy
from apps.common import utils,views
from rest_framework.reverse import reverse
from . import models,admin,forms,serializers

# Create your views here.
class ListaExamenesInternosTemplateView(views.GenericTemplateView):
    template_name = 'lista_examenes_internos.html'

    def get(self, request):
        url = reverse('examenes-internos-list',request=request)
        url_edit = reverse_lazy('editar-examen-interno',kwargs={'pk':0})
        url_add = reverse_lazy('agregar-examen-interno')
        data = self.get_paginator(request=request,model=models.ExInterno)
        campos = admin.ExInternoAdmin.list_display
        campos = utils.format_names(names=campos)
        data['campos']=campos
        data['url']=url
        data['url_edit']=str(url_edit).replace('0/','')
        data['url_add']=url_add
        return render(request=request, template_name=self.template_name,context=data)
        
class ListaExamenesExternosTemplateView(views.GenericTemplateView):
    template_name = 'lista_examenes_externos.html'

    def get(self, request):
        data = self.get_paginator(request=request,model=models.ExLaboratorio)
        campos = admin.ExLaboratorioAdmin.list_display
        campos = utils.format_names(names=campos)
        data['campos']=campos
        return render(request=request, template_name=self.template_name,context=data)
    
# - - - - - - - - - - - - - - - - - - - - - -

class ExamenInternoCreateView(views.GenericTemplateView):
    template_name='agregar_examen_interno.html'

    def get(self, request, *args, **kwargs):
        data={}
        data['form']=forms.ExamenInternoForm
        url = reverse('servicios-list',request=request)
        data['url'] = url
        return render(request=request,template_name=self.template_name,context=data)
    
class ExamenInternoEditView(views.GenericTemplateView):
    template_name = 'editar_examen_interno.html'
    
    def get(self, request, *args, **kwargs):
        # Obtener el producto por su 'pk'
        data={}
        entity = utils.model_or_none(model=models.ExInterno, pk=kwargs['pk'])
        form = forms.ExamenInternoForm(instance=entity)  # Pasa la instancia del modelo existente al formulario
        url = reverse('servicios-list',request=request)
        data['url'] = url
        data['form']=form
        data['entity']=entity
        return render(request=request, template_name=self.template_name,context=data)
    
# ---------------------------------------------------------------- DRF Views
class ExamenInternoViewSet(views.GenericViewSet):
    queryset = models.ExInterno.objects.all()
    serializer_class = serializers.ExamenInternoSerializer