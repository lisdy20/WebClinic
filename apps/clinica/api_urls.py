from rest_framework.routers import DefaultRouter
from django.urls import path, include
from . import views

router = DefaultRouter()
router.register(r'servicios', views.ServicioViewSet, basename='servicios')

urlpatterns = [
    path('', include(router.urls)),
]