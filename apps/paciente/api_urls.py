from rest_framework.routers import DefaultRouter
from django.urls import path, include
from . import views

router = DefaultRouter()
router.register(r'pacientes', views.PacienteViewSet, basename='pacientes')

urlpatterns = [
    path('', include(router.urls)),
]