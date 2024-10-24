from django.shortcuts import render
from django.views.generic import TemplateView
from apps.common import utils,views
from . import admin,models

# Create your views here.
class ListaPacientesTemplateView(views.GenericTemplateView):
    template_name = 'lista_pacientes.html'

    def get(self, request):
        data = self.get_paginator(request=request,model=models.Paciente)
        campos = admin.PacienteAdmin.list_display
        campos = utils.format_names(names=campos)
        data['campos']=campos
        return render(request=request, template_name=self.template_name,context=data)