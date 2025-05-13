from rest_framework import serializers
from sistema.models import *

class usuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = usuario
        fields = '__all__'
        read_only_fields = ['id_usuario','nombre']
    

class zona_de_riegoSerializer(serializers.ModelSerializer):
    class Meta:
        model = zona_riego 
        fields = '__all__'
        read_only_fields = ['id_zona']

class sensorSerializer(serializers.ModelSerializer):
    class Meta:
        model = sensor
        fields = '__all__'
        read_only_fields = ['id_sensor','id_zona']


class configuracionSerializer(serializers.ModelSerializer):
    class Meta:
        model = configuracion_riego
        fields = '__all__'
        read_only_fields = ['id_configuracion','id_zona']

class lectura_sensorSeriaizer(serializers.ModelSerializer):
    class Meta:
        model = lectura_sensor
        fields = '__all__'
        read_only_fields = ['id_lectura','id_sensor']

class historial_riego(serializers.ModelSerializer):
    class Meta:
        model = historial_riego
        fields = '__all__'
        read_only_fields = ['id_historial','id_zona']

class mantenimientoSerializer(serializers.ModelSerializer):
    class Meta:
        model = mantenimiento
        fields = '__all__'
        read_only_fields = ['id_mantenimiento','id_zona']

