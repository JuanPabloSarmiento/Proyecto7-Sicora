from rest_framework import serializers
# Importa el modelo usuario desde la aplicación 'sistema'
from apps.usuarios.models import usuario
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