# api_sicora/urls.py
from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter

# Importa todos los ViewSets
from apps.sistema.views import zona_riegoViewSet, sensorViewSet, configuracion_riegoViewSet, lectura_sensorViewSet
from apps.mantenimiento.views import historial_riegoViewSet, mantenimientoViewSet
from apps.usuarios.views import usuarioViewSet

router = DefaultRouter()
# Registra los ViewSets en el router
router.register(r'usuarios', usuarioViewSet)
router.register(r'zonas', zona_riegoViewSet)
router.register(r'sensores', sensorViewSet)
router.register(r'configuraciones', configuracion_riegoViewSet)
router.register(r'lecturas', lectura_sensorViewSet)
router.register(r'historial', historial_riegoViewSet)
router.register(r'mantenimientos', mantenimientoViewSet)
# Define las URL del proyecto
urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
]
