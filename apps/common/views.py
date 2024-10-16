from django.shortcuts import render
from django.views.generic import TemplateView
from django.core.paginator import Paginator


# Create your views here.
class GenericTemplateView(TemplateView):
    pages_number=20
    enable_paginator = True

    def get_paginator(self,request=None,model=None):
        entity = model.objects.all()
        if self.enable_paginator:
            paginator = Paginator(entity, self.pages_number)
            page_number = request.GET.get('page')
            return paginator.get_page(page_number)
        else:
            return entity