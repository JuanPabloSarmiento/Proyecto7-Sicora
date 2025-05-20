# urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    usuarioViewSet,
    zona_riegoViewSet,
    sensorViewSet,
    configuracion_riegoViewSet,
    lectura_sensorViewSet,
    historial_riegoViewSet,
    mantenimientoViewSet,
)

router = DefaultRouter()
router.register(r'usuarios', usuarioViewSet)
router.register(r'zonas', zona_riegoViewSet)
router.register(r'sensores', sensorViewSet)
router.register(r'configuraciones', configuracion_riegoViewSet)
router.register(r'lecturas', lectura_sensorViewSet)
router.register(r'historial', historial_riegoViewSet)
router.register(r'mantenimientos', mantenimientoViewSet)

urlpatterns = [
    path('', include(router.urls)),
]