from django.db import models

# Modelo de usuario
class usuario(models.Model):
    # Definición de roles como opciones (admin u operario)
    ROLES = [
        ('admin', 'Administrador'),
        ('operario', 'Operario'),
    ]
    # Campos del modelo
    nombre = models.CharField(max_length=50)  # Nombre del usuario
    correo = models.EmailField(max_length=100, unique=True)  # Correo único
    contraseña = models.CharField(max_length=100)  # Contraseña del usuario
    rol = models.CharField(max_length=20, choices=ROLES, default='operario')  # Rol del usuario

    def __str__(self):
        # Retorna el nombre del usuario y su rol (en formato legible)
        return f"{self.nombre} ({self.get_rol_display()})"
