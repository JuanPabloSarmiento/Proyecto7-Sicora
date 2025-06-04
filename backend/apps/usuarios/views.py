from rest_framework import viewsets
# Importa los modelos de la aplicación
from apps.usuarios.models import usuario
# Importa el serializador para el modelo usuario
from apps.usuarios.serializers import usuarioSerializer
# ViewSet para el modelo usuario
class usuarioViewSet(viewsets.ModelViewSet):
    queryset = usuario.objects.all()  # Consulta todos los registros de usuario
    serializer_class = usuarioSerializer  # Serializador para el modelo usuario
    http_method_names = ['get', 'post', 'put', 'delete']  # Métodos HTTP permitidos
