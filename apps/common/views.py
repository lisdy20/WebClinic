from django.views.generic import TemplateView
from django.core.paginator import Paginator
from rest_framework import viewsets
from rest_framework.response import Response


# Create your views here.
class GenericTemplateView(TemplateView):
    elements_per_pages=20
    enable_paginator = True

    def get_paginator(self,request=None,model=None):
        data={}
        entity = model.objects.all()
        if self.enable_paginator:
            paginator = Paginator(entity, self.elements_per_pages)
            page_number = request.GET.get('page')
            page_obj = paginator.get_page(page_number)
            data['paginator'] = paginator
            data['page_obj'] = page_obj
        else:
            data['page_obj']=entity
        return data

class GenericViewSet(viewsets.ModelViewSet):
    def create(self, request, *args, **kwargs):
        response = super().create(request, *args, **kwargs)
        # Enviamos el ID del registro creado como parte de la respuesta
        return Response({'id': response.data['id'], 'detail': 'Registro guardado correctamente'}, status=response.status_code)