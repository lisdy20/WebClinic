from django.shortcuts import render
from django.urls import reverse_lazy
from apps.common import utils,views
from rest_framework.reverse import reverse
from . import models,admin,forms,serializers


class ListaMedicamentoTemplateView(views.GenericTemplateView):
    template_name = 'lista_medicamentos.html'

    def get(self, request):
        url = reverse('medicamentos-list',request=request)
        url_edit = reverse_lazy('editar-medicamento',kwargs={'pk':0})
        url_add = reverse_lazy('agregar-medicamento')
        data = self.get_paginator(request=request,model=models.Medicamento)
        campos = admin.MedicamentoAdmin.list_display
        campos = utils.format_names(names=campos)
        data['campos']=campos
        data['url']=url
        data['url_edit']=str(url_edit).replace('0/','')
        data['url_add']=str(url_add)
        return render(request=request, template_name=self.template_name,context=data)
    

# ----------------------------------------------------------------
class MedicamentoCreateView(views.GenericTemplateView):
    template_name='agregar_medicamento.html'

    def get(self, request, *args, **kwargs):
        data={}
        
        data['form']=forms.MedicamentoForm
        url = reverse('medicamentos-list',request=request)
        url_list = reverse_lazy('lista-medicamentos')
        url_edit = reverse_lazy('editar-medicamento',kwargs={'pk':0})
        data['url'] = url
        data['url_edit'] = str(url_edit).replace('0/','')
        data['url_list'] = url_list
        return render(request=request,template_name=self.template_name,context=data)
    
# ---------------------------------------------------------------- DRF Views

class MedicamentoViewSet(views.GenericViewSet):
    queryset = models.Medicamento.objects.all()
    serializer_class = serializers.MedicamentoSerializer

# ----------------------------------------------------------------