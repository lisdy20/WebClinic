from rest_framework.routers import DefaultRouter
from django.urls import path, include
from . import views

router = DefaultRouter()
router.register(r'examenes-internos', views.ExamenInternoViewSet, basename='examenes-internos')

urlpatterns = [
    path('', include(router.urls)),
]