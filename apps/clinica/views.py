from django.shortcuts import render
from django.views.generic import TemplateView
from apps.common import utils,views
from . import models,admin

# Create your views here.
class ListaCitaTemplateView(views.GenericTemplateView):
    template_name = 'lista_citas.html'

    def get(self, request):
        page_obj = self.get_paginator(request=request,model=models.Cita)
        campos = admin.CitaAdmin.list_display
        campos = utils.format_names(names=campos)
        data={'page_obj': page_obj,'campos':campos}
        return render(request=request, template_name=self.template_name,context=data)