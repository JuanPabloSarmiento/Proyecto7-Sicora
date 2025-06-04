# Importa la función 'path' para definir rutas y 'include' para incluir rutas de otros módulos
from django.urls import path, include

# Importa el enrutador por defecto de Django REST Framework
from rest_framework.routers import DefaultRouter
# Importa los viewsets de la aplicación
from apps.mantenimiento.views import(
    historial_riegoViewSet, mantenimientoViewSet
)
router = DefaultRouter()
# Registra cada viewset con un prefijo de URL
router.register(r'historial', historial_riegoViewSet)  # ViewSet para historial de riego
router.register(r'mantenimientos', mantenimientoViewSet)  # ViewSet para mantenimientos
# Define las URL del proyecto
urlpatterns = [
    # Incluye todas las rutas generadas automáticamente por el router
    path('', include(router.urls)),
]