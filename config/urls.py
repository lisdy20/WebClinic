"""
URL configuration for config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include, re_path
from apps.configuracion import views
from django.views.static import serve
from django.conf import settings
from django.conf.urls.static import static

from apps.configuracion import urls

urlpatterns = [
    re_path(r'^media/(?P<path>.*)$', serve,{'document_root': settings.MEDIA_ROOT}),
    re_path(r'^static/(?P<path>.*)$', serve,{'document_root': settings.STATIC_ROOT}),
    path('admin/', admin.site.urls),
    path('', views.InicioTemplateView.as_view()),
    path('usuarios/', include('apps.usuarios.urls')),
    path('clinica/', include('apps.clinica.urls')),
    path('pacientes/', include('apps.paciente.urls')),
    path('pagos/', include('apps.pagos.urls')),
    path('examenes/', include('apps.examenes.urls')),
    path('medicamentos/', include('apps.medicamentos.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    path('api-auth/', include('rest_framework.urls')),
    path('api/',include('apps.api.urls')),
] + urls.urlpatterns

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
else:
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)