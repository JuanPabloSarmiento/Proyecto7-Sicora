# Importa viewsets de Django REST Framework
from rest_framework import viewsets

# Importa los modelos de la aplicación
from apps.sistema.models import (
    zona_riego, sensor, configuracion_riego, 
    lectura_sensor
)

# Importa los serializadores de la aplicación
from apps.sistema.serializers import (
    zona_riegoSerializer, sensorSerializer, 
    configuracion_riegoSerializer, lectura_sensorSerializer
)

# ViewSet para el modelo zona_riego
class zona_riegoViewSet(viewsets.ModelViewSet):
    queryset = zona_riego.objects.all()  # Consulta todas las zonas de riego
    serializer_class = zona_riegoSerializer  # Serializador para el modelo zona_riego
    http_method_names = ['get', 'post', 'put', 'delete']  # Métodos HTTP permitidos

# ViewSet para el modelo sensor
class sensorViewSet(viewsets.ModelViewSet):
    queryset = sensor.objects.all()  # Consulta todos los registros de sensores
    serializer_class = sensorSerializer  # Serializador para el modelo sensor
    http_method_names = ['get', 'post', 'put', 'delete']  # Métodos HTTP permitidos

# ViewSet para el modelo configuracion_riego
class configuracion_riegoViewSet(viewsets.ModelViewSet):
    queryset = configuracion_riego.objects.all()  # Consulta todas las configuraciones de riego
    serializer_class = configuracion_riegoSerializer  # Serializador para el modelo configuracion_riego
    http_method_names = ['get', 'post', 'put', 'delete']  # Métodos HTTP permitidos

# ViewSet para el modelo lectura_sensor
class lectura_sensorViewSet(viewsets.ModelViewSet):
    queryset = lectura_sensor.objects.all()  # Consulta todas las lecturas de sensores
    serializer_class = lectura_sensorSerializer  # Serializador para el modelo lectura_sensor
    http_method_names = ['get', 'post', 'put', 'delete']  # Métodos HTTP permitidos
    
