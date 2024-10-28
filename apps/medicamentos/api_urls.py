from rest_framework.routers import DefaultRouter
from django.urls import path, include
from . import views

router = DefaultRouter()
router.register(r'medicamentos', views.MedicamentoViewSet, basename='medicamentos')
router.register(r'receta-medica', views.RecetaMedicaViewSet, basename='receta-medica')
router.register(r'detalles-receta', views.DetalleRecetaViewSet, basename='detalles-receta')

urlpatterns = [
    path('', include(router.urls)),
]