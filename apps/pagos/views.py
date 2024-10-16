from django.shortcuts import render
from django.core.paginator import Paginator
from apps.common import views,utils
from . import models,admin


# Create your views here.
class PagosListTemplateView(views.GenericTemplateView):
    template_name = 'lista_pagos.html'
    def get(self, request):
        page_obj = self.get_paginator(request=request,model=models.ControlPago)
        campos = admin.ControlPagoAdmin.list_display
        campos = utils.format_names(names=campos)
        data={'page_obj': page_obj,'campos':campos}
        return render(request=request, template_name=self.template_name,context=data)