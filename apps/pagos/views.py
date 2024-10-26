from django.http.response import HttpResponse as HttpResponse
from django.shortcuts import render
from apps.common import utils,views
from django.urls import reverse_lazy
from rest_framework.reverse import reverse
from rest_framework import viewsets
from . import models,admin,serializers,forms

# Create your views here.
class PagosListTemplateView(views.GenericTemplateView):
    template_name = 'lista_pagos.html'

    def get(self, request):
        url = reverse('pagos-list',request=request)
        url_edit = reverse_lazy('editar-pago',kwargs={'pk':0})
        url_add = reverse_lazy('agregar-pago')
        data = self.get_paginator(request=request,model=models.ControlPago)
        campos = admin.ControlPagoAdmin.list_display
        campos = utils.format_names(names=campos)
        data['campos']=campos
        data['url']=url
        data['url_edit']=str(url_edit).replace('0/','')
        data['url_add']=str(url_add)
        return render(request=request, template_name=self.template_name,context=data)
    
# ----------------------------------------------------------------

class PagosCreateView(views.GenericTemplateView):
    template_name='agregar_pago.html'

    def get(self, request, *args, **kwargs):
        data={}
        
        data['form']=forms.ControlPagoForm
        url = reverse('pagos-list',request=request)
        url_list = reverse_lazy('lista-pagos')
        url_edit = reverse_lazy('editar-pago',kwargs={'pk':0})
        data['url'] = url
        data['url_edit'] = str(url_edit).replace('0/','')
        data['url_list'] = url_list
        return render(request=request,template_name=self.template_name,context=data)
    
class PagoEditView(views.GenericTemplateView):
    template_name = 'editar_pago.html'
    
    def get(self, request, *args, **kwargs):
        # Obtener el producto por su 'pk'
        data={}
        entity = utils.model_or_none(model=models.ControlPago, pk=kwargs['pk'])
        form = forms.ControlPagoForm(instance=entity)  # Pasa la instancia del modelo existente al formulario
        url = reverse('pagos-list',request=request)
        url_list = reverse_lazy('lista-pagos')
        data['id']=kwargs['pk']
        data['url'] = url
        data['url_list'] = url_list
        data['form']=form
        data['entity']=entity
        return render(request=request, template_name=self.template_name,context=data)
    
# ---------------------------------------------------------------- Views DRF

class ControlPagoViewSet(views.GenericViewSet):
    queryset = models.ControlPago.objects.all()
    serializer_class = serializers.ControlPagoSerializer