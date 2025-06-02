# Importa el módulo serializers de Django REST Framework
from rest_framework import serializers
# Importa el modelo usuario desde la aplicación 'sistema'
from apps.mantenimiento.models import historial_riego, mantenimiento
# Serializador para el modelo historial_riego
class historial_riegoSerializer(serializers.ModelSerializer):
    class Meta:
        model = historial_riego  # Modelo a serializar
        fields = ('id', 'fecha', 'duracion', 'cantidad_agua')
        read_only_fields = ['id']

# Serializador para el modelo mantenimiento
class mantenimientoSerializer(serializers.ModelSerializer):
    class Meta:
        model = mantenimiento  # Modelo a serializar
        fields = ('id', 'fecha', 'descripcion', 'tipo')
        read_only_fields = ['id']