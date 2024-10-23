from rest_framework.routers import DefaultRouter
from django.urls import path, include
from . import views

router = DefaultRouter()
router.register(r'medicamentos', views.MedicamentoViewSet, basename='medicamentos')

urlpatterns = [
    path('', include(router.urls)),
]