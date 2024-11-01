from django.shortcuts import render
from django.urls import reverse_lazy
from apps.common import utils,views
from rest_framework.reverse import reverse
from rest_framework.parsers import MultiPartParser, FormParser
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
        url = reverse('examenes-externos-list',request=request)
        url_edit = reverse_lazy('editar-examen-externo',kwargs={'pk':0})
        url_add = reverse_lazy('agregar-examen-externo')
        data = self.get_paginator(request=request,model=models.ExLaboratorio)
        campos = admin.ExLaboratorioAdmin.list_display
        campos = utils.format_names(names=campos)
        data['campos']=campos
        data['url']=url
        data['url_edit']=str(url_edit).replace('0/','')
        data['url_add']=url_add
        return render(request=request, template_name=self.template_name,context=data)
    
# - - - - - - - - - - - - - - - - - - - - - -

class ExamenInternoCreateView(views.GenericTemplateView):
    template_name='agregar_examen_interno.html'

    def get(self, request, *args, **kwargs):
        data={}
        
        data['form']=forms.ExamenInternoForm
        url = reverse('examenes-internos-list',request=request)
        url_list = reverse_lazy('lista-examenes-internos')
        url_edit = reverse_lazy('editar-examen-interno',kwargs={'pk':0})
        data['url'] = url
        data['url_edit'] = str(url_edit).replace('0/','')
        data['url_list'] = url_list
        return render(request=request,template_name=self.template_name,context=data)
    
class ExamenInternoEditView(views.GenericTemplateView):
    template_name = 'editar_examen_interno.html'
    
    def get(self, request, *args, **kwargs):
        # Obtener el producto por su 'pk'
        data={}
        entity = utils.model_or_none(model=models.ExInterno, pk=kwargs['pk'])
        form = forms.ExamenInternoForm(instance=entity)  # Pasa la instancia del modelo existente al formulario
        formdocumento = forms.DocResInternoForm
        url = reverse('examenes-internos-list',request=request)
        url_api_documento = reverse('documentos-internos-list',request=request)
        url_list = reverse_lazy('lista-examenes-internos')
        data['id']=kwargs['pk']
        data['url'] = url
        data['url_api_documento'] = url_api_documento
        data['url_list'] = url_list
        data['form']=form
        data['formdocumento']=formdocumento
        data['entity']=entity
        return render(request=request, template_name=self.template_name,context=data)
    

class ExamenExternoCreateView(views.GenericTemplateView):
    template_name='agregar_examen_externo.html'

    def get(self, request, *args, **kwargs):
        data={}
        
        data['form']=forms.ExLaboratorioForm
        url = reverse('examenes-externos-list',request=request)
        url_list = reverse_lazy('lista-examenes-externos')
        url_edit = reverse_lazy('editar-examen-externo',kwargs={'pk':0})
        data['url'] = url
        data['url_edit'] = str(url_edit).replace('0/','')
        data['url_list'] = url_list
        return render(request=request,template_name=self.template_name,context=data)
    
class ExamenExternoEditView(views.GenericTemplateView):
    template_name = 'editar_examen_externo.html'
    
    def get(self, request, *args, **kwargs):
        # Obtener el producto por su 'pk'
        data={}
        entity = utils.model_or_none(model=models.ExLaboratorio, pk=kwargs['pk'])
        form = forms.ExLaboratorioForm(instance=entity)  # Pasa la instancia del modelo existente al formulario
        url = reverse('examenes-externos-list',request=request)
        url_list = reverse_lazy('lista-examenes-externos')
        data['id']=kwargs['pk']
        data['url'] = url
        data['url_list'] = url_list
        data['form']=form
        data['entity']=entity
        return render(request=request, template_name=self.template_name,context=data)
    
# ---------------------------------------------------------------- DRF Views
class ExamenInternoViewSet(views.GenericViewSet):
    queryset = models.ExInterno.objects.filter(activo=True)
    serializer_class = serializers.ExamenInternoSerializer

class DocInternoViewSet(views.GenericViewSet):
    queryset = models.DocResInterno.objects.filter(activo=True)
    serializer_class = serializers.DocInternoSerializer

class ExamenExternoViewSet(views.GenericViewSet):
    queryset = models.ExInterno.objects.filter(activo=True)
    serializer_class = serializers.ExamenExternoSerializer