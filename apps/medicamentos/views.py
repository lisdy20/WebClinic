from django.http.response import HttpResponse as HttpResponse
from django.shortcuts import render
from apps.common import utils,views
from rest_framework.reverse import reverse
from rest_framework import viewsets
from . import models,admin,serializers,forms


class ListaMedicamentoTemplateView(views.GenericTemplateView):
    template_name = 'lista_medicamentos.html'

    def get(self, request):
        url = reverse('medicamentos-list',request=request)
        data = self.get_paginator(request=request,model=models.Medicamento)
        campos = admin.MedicamentoAdmin.list_display
        campos = utils.format_names(names=campos)
        data['campos']=campos
        data['url']=url
        return render(request=request, template_name=self.template_name,context=data)
    

# ----------------------------------------------------------------
class MedicamentoCreateView(views.GenericTemplateView):
    template_name='agregar_medicamento.html'

    def get(self, request, *args, **kwargs):
        data={}
        data['form']=forms.MedicamentoForm
        url = reverse('medicamentos-list',request=request)
        # Pasar el mensaje al contexto si existe en la sesión
        data['url'] = url
        return render(request=request,template_name=self.template_name,context=data)
    
# ---------------------------------------------------------------- DRF Views

class MedicamentoViewSet(viewsets.ModelViewSet):
    queryset = models.Medicamento.objects.all()
    serializer_class = serializers.MedicamentoSerializer

# ----------------------------------------------------------------