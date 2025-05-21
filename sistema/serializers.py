from rest_framework import serializers
from sistema.models import (
    usuario, zona_riego, sensor, 
    configuracion_riego,
    lectura_sensor,
    historial_riego,
    mantenimiento,
)

class usuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = usuario
        fields = ('id_usuario', 'nombre', 'correo', 'contraseña', 'rol')
        read_only_fields = ['id_usuario']
    

class zona_riegoSerializer(serializers.ModelSerializer):
    class Meta:
        model = zona_riego 
        fields = ('id_zona', 'nombre_zona', 'tipo_planta', 'necesidades_hidricas', 'exposicion_solar')
        read_only_fields = ['id_zona']

class sensorSerializer(serializers.ModelSerializer):
    class Meta:
        model = sensor
        fields = ('id_sensor', 'tipo', 'estado')
        read_only_fields = ['id_sensor']


class configuracionSerializer(serializers.ModelSerializer):
    class Meta:
        model = configuracion_riego
        fields = ('id_configuracion', 'frecuencia', 'hora_inicio', 'duracion', 'tipo_riego', 'caudal', 'presion')
        read_only_fields = ['id_configuracion']

class lectura_sensorSeriaizer(serializers.ModelSerializer):
    class Meta:
        model = lectura_sensor
        fields = ('id_lectura', 'fecha_hora', 'valor')
        read_only_fields = ['id_lectura']

class historial_riego(serializers.ModelSerializer):
    class Meta:
        model = historial_riego
        fields = ('id_historial', 'fecha', 'duracion', 'cantidad_agua')
        read_only_fields = ['id_historial']

class mantenimientoSerializer(serializers.ModelSerializer):
    class Meta:
        model = mantenimiento
        fields = ('id_mantenimiento', 'fecha', 'descripcion', 'tipo')
        read_only_fields = ['id_mantenimiento']

