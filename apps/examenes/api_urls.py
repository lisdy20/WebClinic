from rest_framework.routers import DefaultRouter
from django.urls import path, include
from . import views

router = DefaultRouter()
router.register(r'examenes-internos', views.ExamenInternoViewSet, basename='examenes-internos')
router.register(r'documentos-internos', views.DocInternoViewSet, basename='documentos-internos')
router.register(r'examenes-externos', views.ExamenExternoViewSet, basename='examenes-externos')

urlpatterns = [
    path('', include(router.urls)),
]