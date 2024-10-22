from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('clinica/', include('apps.clinica.api_urls')),  # Incluye las URLs de la aplicación que contiene el router
]