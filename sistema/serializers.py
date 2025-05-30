# Importa el módulo serializers de Django REST Framework
from rest_framework import serializers

# Importa los modelos definidos en la aplicación 'sistema'
from sistema.models import (
    usuario, zona_riego, sensor, 
    configuracion_riego,
    lectura_sensor,
    historial_riego,
    mantenimiento,
)

# Serializador para el modelo usuario
class usuarioSerializer(serializers.ModelSerializer):
    # Campo adicional para mostrar el rol de forma legible (usando get_rol_display)
    rol_display = serializers.CharField(source='get_rol_display', read_only=True)

    class Meta:
        model = usuario  # Modelo a serializar
        # Campos a incluir en la serialización
        fields = ('id', 'nombre', 'correo', 'contraseña', 'rol', 'rol_display')
        # Configuración adicional: contraseña y rol solo escritura, id solo lectura
        extra_kwargs = {
            'contraseña': {'write_only': True},
            'rol': {'write_only': True}
        }
        read_only_fields = ['id']

# Serializador para el modelo zona_riego
class zona_riegoSerializer(serializers.ModelSerializer):
    class Meta:
        model = zona_riego  # Modelo a serializar
        fields = ('id', 'nombre_zona', 'tipo_planta', 'necesidades_hidricas', 'exposicion_solar')
        read_only_fields = ['id']  # id solo lectura

# Serializador para el modelo sensor
class sensorSerializer(serializers.ModelSerializer):
    class Meta:
        model = sensor  # Modelo a serializar
        fields = ('id', 'tipo', 'estado')
        read_only_fields = ['id']

# Serializador para el modelo configuracion_riego
class configuracion_riegoSerializer(serializers.ModelSerializer):
    class Meta:
        model = configuracion_riego  # Modelo a serializar
        fields = ('id', 'frecuencia', 'hora_inicio', 'duracion', 'tipo_riego', 'caudal', 'presion')
        read_only_fields = ['id']

# Serializador para el modelo lectura_sensor
class lectura_sensorSeriaizer(serializers.ModelSerializer):
    class Meta:
        model = lectura_sensor  # Modelo a serializar
        fields = ('id', 'fecha_hora', 'valor')
        read_only_fields = ['id']

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
# Fin del archivo sistema/serializers.py
