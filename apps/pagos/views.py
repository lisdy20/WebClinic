from django.http import HttpRequest
from django.http.response import HttpResponse as HttpResponse
from django.shortcuts import render
from apps.common import utils,views
from rest_framework.reverse import reverse
from rest_framework import viewsets
from . import models,admin,serializers,forms

# Create your views here.
class PagosListTemplateView(views.GenericTemplateView):
    template_name = 'lista_pagos.html'
    def get(self, request):
        url = reverse('pagos-list',request=request)
        data = self.get_paginator(request=request,model=models.ControlPago)
        campos = admin.ControlPagoAdmin.list_display
        campos = utils.format_names(names=campos)
        data['campos']=campos
        data['url']=url
        return render(request=request, template_name=self.template_name,context=data)
    
# ----------------------------------------------------------------

class PagosCreateView(views.GenericTemplateView):
    template_name='agregar_pago.html'

    def get(self, request, *args, **kwargs):
        data={}
        data['form']=forms.ControlPagoForm
        url = reverse('pagos-list',request=request)
        # Pasar el mensaje al contexto si existe en la sesión
        data['url'] = url
        return render(request=request, template_name=self.template_name,context=data)
    
    
# ---------------------------------------------------------------- Views DRF

class ControlPagoViewSet(viewsets.ModelViewSet):
    queryset = models.ControlPago.objects.all()
    serializer_class = serializers.ControlPagoSerializer