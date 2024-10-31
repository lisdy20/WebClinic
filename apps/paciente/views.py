from django.shortcuts import render
from django.urls import reverse_lazy
from apps.common import utils,views
from rest_framework.reverse import reverse
from . import models,admin,forms,serializers

# Create your views here.
class ListaPacientesTemplateView(views.GenericTemplateView):
    template_name = 'lista_pacientes.html'

    def get(self, request):
        url = reverse('pacientes-list',request=request)
        url_edit = reverse_lazy('editar-paciente',kwargs={'pk':0})
        url_add = reverse_lazy('agregar-paciente')
        data = self.get_paginator(request=request,model=models.Paciente)
        campos = admin.PacienteAdmin.list_display
        campos = utils.format_names(names=campos)
        data['campos']=campos
        data['url']=url
        data['url_edit']=str(url_edit).replace('0/','')
        data['url_add']=str(url_add)
        return render(request=request, template_name=self.template_name,context=data)
    
# - - - - - - - - - - - - - - - - - - - - - -
    
class PacienteCreateView(views.GenericTemplateView):
    template_name='agregar_paciente.html'

    def get(self, request, *args, **kwargs):
        data={}
        
        data['form']=forms.PacienteForm
        url = reverse('pacientes-list',request=request)
        url_list = reverse_lazy('lista-pacientes')
        url_edit = reverse_lazy('editar-paciente',kwargs={'pk':0})
        data['url'] = url
        data['url_edit'] = str(url_edit).replace('0/','')
        data['url_list'] = url_list
        return render(request=request,template_name=self.template_name,context=data)
    

class PacienteEditView(views.GenericTemplateView):
    template_name = 'editar_paciente.html'
    
    def get(self, request, *args, **kwargs):
        # Obtener el producto por su 'pk'
        data={}
        entity = utils.model_or_none(model=models.Paciente, pk=kwargs['pk'])
        form = forms.PacienteForm(instance=entity)  # Pasa la instancia del modelo existente al formulario
        url = reverse('pacientes-list',request=request)
        url_list = reverse_lazy('lista-pacientes')
        data['id']=kwargs['pk']
        data['url'] = url
        data['url_list'] = url_list
        data['form']=form
        data['entity']=entity
        return render(request=request, template_name=self.template_name,context=data)
    
class AntecedenteEditView(views.GenericTemplateView):
    template_name = 'editar_antecedente.html'
    
    def get(self, request, *args, **kwargs):
        # Obtener el producto por su 'pk'
        data={}
        entity = utils.model_or_none(model=models.Paciente, pk=kwargs['pk'])
        print(entity)
        antecedentes = models.Antecedente.objects.filter(paciente=entity,activo=True)
        form = forms.AntecedenteForm(instance=entity)  # Pasa la instancia del modelo existente al formulario
        url = reverse('antecedentes-list',request=request)
        url_cita = reverse_lazy('editar-cita',kwargs={'pk':0})
        url_list = ''
        data['id']=kwargs['pk']
        data['url'] = url
        data['url_cita'] = str(url_cita).replace('0/','')
        data['url_list'] = url_list
        data['form']=form
        data['antecedentes']=antecedentes
        data['entity']=entity
        return render(request=request, template_name=self.template_name,context=data)
    

# - - - - - - - - - - - - - - - - - - - - - - Views DRF

class PacienteViewSet(views.GenericViewSet):
    queryset = models.Paciente.objects.filter(activo=True)
    serializer_class = serializers.PacienteSerializer


class AntecedenteViewSet(views.GenericViewSet):
    queryset = models.Antecedente.objects.filter(activo=True)
    serializer_class = serializers.AntecedenteSerializer