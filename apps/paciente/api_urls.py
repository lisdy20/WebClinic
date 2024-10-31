from rest_framework.routers import DefaultRouter
from django.urls import path, include
from . import views

router = DefaultRouter()
router.register(r'pacientes', views.PacienteViewSet, basename='pacientes')
router.register(r'antecedentes', views.AntecedenteViewSet, basename='antecedentes')

urlpatterns = [
    path('', include(router.urls)),
]