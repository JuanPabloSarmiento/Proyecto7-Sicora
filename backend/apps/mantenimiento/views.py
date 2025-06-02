# Importa viewsets de Django REST Framework
from rest_framework import viewsets
# Importa los modelos de la aplicación
from apps.mantenimiento.models import ( historial_riego, mantenimiento)
# Importa los serializadores de la aplicación
from apps.mantenimiento.serializers import (historial_riegoSerializer, mantenimientoSerializer)

# ViewSet para el modelo historial_riego
class historial_riegoViewSet(viewsets.ModelViewSet):
    queryset = historial_riego.objects.all()  # Consulta todos los historiales de riego
    serializer_class = historial_riegoSerializer  # Serializador para el modelo historial_riego
    http_method_names = ['get']  # Métodos HTTP permitidos

# ViewSet para el modelo mantenimiento
class mantenimientoViewSet(viewsets.ModelViewSet):
    queryset = mantenimiento.objects.all()  # Consulta todos los mantenimientos
    serializer_class = mantenimientoSerializer  # Serializador para el modelo mantenimiento
    http_method_names = ['get', 'post', 'put', 'delete']  # Métodos HTTP permitidos   