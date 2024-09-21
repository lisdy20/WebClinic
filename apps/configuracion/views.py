from typing import Any
from django.http import HttpRequest
from django.http.response import HttpResponse as HttpResponse
from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.
class InicioTemplateView(TemplateView):
    template_name = 'index.html'

    def get(self, request):
        return render(request=request, template_name=self.template_name)