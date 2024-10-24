from django.shortcuts import render
from apps.common import views,utils
from . import models,admin

# Create your views here.
class UsuariosTemplateView(views.TemplateView):
    template_name = 'usuarios.html'
    def get(self, request):
        return render(request=request, template_name=self.template_name)

class UsuariosListTemplateView(views.GenericTemplateView):
    template_name = 'lista_usuarios.html'
    def get(self, request):
        
        data = self.get_paginator(request=request,model=models.Perfil)
        campos = admin.PerfilAdmin.list_display
        campos = utils.format_names(names=campos)
        data['campos']=campos
        return render(request=request, template_name=self.template_name,context=data)