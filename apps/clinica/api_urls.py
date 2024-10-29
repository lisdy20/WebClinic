from rest_framework.routers import DefaultRouter
from django.urls import path, include
from . import views

router = DefaultRouter()
router.register(r'servicios', views.ServicioViewSet, basename='servicios')
router.register(r'citas', views.CitaViewSet, basename='citas')
router.register(r'detalles-citas', views.DetalleCitaViewSet, basename='detalles-citas')
router.register(r'historiales', views.HistorialViewSet, basename='historiales')

urlpatterns = [
    path('', include(router.urls)),
]