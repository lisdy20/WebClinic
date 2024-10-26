from rest_framework.routers import DefaultRouter
from django.urls import path, include
from . import views

router = DefaultRouter()
router.register(r'empleados', views.PerfilViewSet, basename='empleados')

urlpatterns = [
    path('', include(router.urls)),
]