from django.shortcuts import render
from apps.common import utils,views
from . import admin,models

# Create your views here.
class ListaExamenesInternosTemplateView(views.GenericTemplateView):
    template_name = 'lista_examenes_internos.html'

    def get(self, request):
        data = self.get_paginator(request=request,model=models.ExInterno)
        campos = admin.ExInternoAdmin.list_display
        campos = utils.format_names(names=campos)
        data['campos']=campos
        return render(request=request, template_name=self.template_name,context=data)
    
class ListaExamenesExternosTemplateView(views.GenericTemplateView):
    template_name = 'lista_examenes_externos.html'

    def get(self, request):
        data = self.get_paginator(request=request,model=models.ExLaboratorio)
        campos = admin.ExLaboratorioAdmin.list_display
        campos = utils.format_names(names=campos)
        data['campos']=campos
        return render(request=request, template_name=self.template_name,context=data)
    
    