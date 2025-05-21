from rest_framework import serializers
from sistema.models import (
    usuario, zona_riego, sensor, 
    configuracion_riego,
    lectura_sensor,
    historial_riego,
    mantenimiento,
)

class usuarioSerializer(serializers.ModelSerializer):
    rol_display = serializers.CharField(source='get_rol_display', read_only=True)
    class Meta:
        model = usuario
        fields = ('id', 'nombre', 'correo', 'contraseña', 'rol', 'rol_display')
        extra_kwargs = {
            'contraseña': {'write_only': True},
            'rol': {'write_only': True}
        }
        read_only_fields = ['id']
    

class zona_riegoSerializer(serializers.ModelSerializer):
    class Meta:
        model = zona_riego 
        fields = ('id', 'nombre_zona', 'tipo_planta', 'necesidades_hidricas', 'exposicion_solar')
        read_only_fields = ['id']

class sensorSerializer(serializers.ModelSerializer):
    class Meta:
        model = sensor
        fields = ('id', 'tipo', 'estado')
        read_only_fields = ['id']


class configuracionSerializer(serializers.ModelSerializer):
    class Meta:
        model = configuracion_riego
        fields = ('id', 'frecuencia', 'hora_inicio', 'duracion', 'tipo_riego', 'caudal', 'presion')
        read_only_fields = ['id']

class lectura_sensorSeriaizer(serializers.ModelSerializer):
    class Meta:
        model = lectura_sensor
        fields = ('id', 'fecha_hora', 'valor')
        read_only_fields = ['id']

class historial_riegoSerializer(serializers.ModelSerializer):
    class Meta:
        model = historial_riego
        fields = ('id', 'fecha', 'duracion', 'cantidad_agua')
        read_only_fields = ['id']

class mantenimientoSerializer(serializers.ModelSerializer):
    class Meta:
        model = mantenimiento
        fields = ('id', 'fecha', 'descripcion', 'tipo')
        read_only_fields = ['id']

