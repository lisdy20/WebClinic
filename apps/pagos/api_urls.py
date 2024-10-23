from rest_framework.routers import DefaultRouter
from django.urls import path, include
from . import views

router = DefaultRouter()
router.register(r'pagos', views.ControlPagoViewSet, basename='pagos')

urlpatterns = [
    path('', include(router.urls)),
]