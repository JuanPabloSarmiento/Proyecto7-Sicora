# Importa la función 'path' para definir rutas y 'include' para incluir rutas de otros módulos
from django.urls import path, include

# Importa el enrutador por defecto de Django REST Framework
from rest_framework.routers import DefaultRouter

# Importa los viewsets de la aplicación
from apps.sistema.views import (
    zona_riegoViewSet,
    sensorViewSet,
    configuracion_riegoViewSet,
    lectura_sensorViewSet
)
# Importa los viewsets de la aplicación de usuarios y mantenimiento
from apps.usuarios.views import usuarioViewSet
from apps.mantenimiento.views import(
    historial_riegoViewSet, mantenimientoViewSet
)
# Crea una instancia del enrutador por defecto
router = DefaultRouter()

# Registra cada viewset con un prefijo de URL
router.register(r'usuarios', usuarioViewSet)  # ViewSet para usuarios
router.register(r'zonas', zona_riegoViewSet)  # ViewSet para zonas de riego
router.register(r'sensores', sensorViewSet)  # ViewSet para sensores
router.register(r'configuraciones', configuracion_riegoViewSet)  # ViewSet para configuraciones de riego
router.register(r'lecturas', lectura_sensorViewSet)  # ViewSet para lecturas de sensor
router.register(r'historial', historial_riegoViewSet)  # ViewSet para historial de riego
router.register(r'mantenimientos', mantenimientoViewSet)  # ViewSet para mantenimientos

# Define las URL del proyecto
urlpatterns = [
    # Incluye todas las rutas generadas automáticamente por el router bajo el prefijo 'api/'
    path('api/', include(router.urls)),
]
