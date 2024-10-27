from django.shortcuts import render
from django.urls import reverse_lazy
from apps.common import utils,views
from rest_framework.reverse import reverse
from . import models,admin,forms,serializers

# Create your views here.
class UsuariosTemplateView(views.TemplateView):
    template_name = 'usuarios.html'
    def get(self, request):
        return render(request=request, template_name=self.template_name)

class UsuariosListTemplateView(views.GenericTemplateView):
    template_name = 'lista_empleados.html'
    
    def get(self, request):
        url = reverse('empleados-list',request=request)
        url_edit = reverse_lazy('editar-empleado',kwargs={'pk':0})
        url_add = reverse_lazy('agregar-empleado')
        data = self.get_paginator(request=request,model=models.Perfil)
        campos = admin.PerfilAdmin.list_display
        campos = utils.format_names(names=campos)
        data['campos']=campos
        data['url']=url
        data['url_edit']=str(url_edit).replace('0/','')
        data['url_add']=str(url_add)
        return render(request=request, template_name=self.template_name,context=data)
    
#------------------------------------------------------------
    
class EmpleadoCreateView(views.GenericTemplateView):
    template_name='agregar_empleado.html'

    def get(self, request, *args, **kwargs):
        data={}
        
        data['form']=forms.PerfilCreateForm
        url = reverse('empleados-list',request=request)
        url_list = reverse_lazy('lista-empleados')
        url_edit = reverse_lazy('editar-empleado',kwargs={'pk':0})
        data['url'] = url
        data['url_edit'] = str(url_edit).replace('0/','')
        data['url_list'] = url_list
        return render(request=request,template_name=self.template_name,context=data)
    

class EmpleadoEditView(views.GenericTemplateView):
    template_name = 'editar_empleado.html'
    
    def get(self, request, *args, **kwargs):
        # Obtener el producto por su 'pk'
        data={}
        entity = utils.model_or_none(model=models.Perfil, pk=kwargs['pk'])
        form = forms.PerfilChangeForm(instance=entity)  # Pasa la instancia del modelo existente al formulario
        url = reverse('servicios-list',request=request)
        url_list = reverse_lazy('lista-servicios')
        data['id']=kwargs['pk']
        data['url'] = url
        data['url_list'] = url_list
        data['form']=form
        data['entity']=entity
        return render(request=request, template_name=self.template_name,context=data)

#---------------------------------------------------------------- Views DRF    

class PerfilViewSet(views.GenericViewSet):
    queryset = models.Perfil.objects.filter(activo=True)
    serializer_class = serializers.PerfilSerializer