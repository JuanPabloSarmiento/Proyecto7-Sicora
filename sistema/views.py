from rest_framework import viewsets
from .models import ( usuario, zona_riego, sensor, configuracion_riego, lectura_sensor, historial_riego, mantenimiento )
from .serializers import ( usuarioSerializer, zona_riegoSerializer, sensorSerializer, configuracion_riegoSerializer, lectura_sensorSerializer, historial_riegoSerializer, mantenimientoSerializer )

class usuarioViewSet(viewsets.ModelViewSet):
    queryset = usuario.objects.all()
    serializer_class = usuarioSerializer
    http_method_names = ['get', 'post', 'put', 'delete']

class zona_riegoViewSet(viewsets.ModelViewSet):
    queryset = zona_riego.objects.all()
    serializer_class = zona_riegoSerializer
    http_method_names = ['get', 'post', 'put', 'delete']

class sensorViewSet(viewsets.ModelViewSet):
    queryset = sensor.objects.all()
    serializer_class =  sensorSerializer
    http_method_names = ['get', 'post', 'put', 'delete']

class configuracion_riegoViewSet(viewsets.ModelViewSet):
    queryset = configuracion_riego.objects.all()
    serializer_class = configuracion_riegoSerializer
    http_method_names = ['get', 'post', 'put', 'delete']

class lectura_sensorViewSet(viewsets.ModelViewSet):
    queryset = lectura_sensor.objects.all()
    serializer_class = lectura_sensorSerializer
    http_method_names = ['get', 'post', 'put', 'delete']

class historial_riegoViewSet(viewsets.ModelViewSet):
    queryset =  historial_riego.objects.all()
    serializer_class = historial_riegoSerializer
    http_method_names = ['get', 'post', 'put', 'delete']

class mantenimientoViewSet(viewsets.ModelViewSet):
    queryset =  mantenimiento.objects.all()
    serializer_class = mantenimientoSerializer
    http_method_names = ['get', 'post', 'put', 'delete']
