from django.db import models

# Modelo de historial de riego
class historial_riego(models.Model):
    # Campos del historial
    fecha = models.DateField()  # Fecha del riego
    duracion = models.TimeField()  # Duración del riego
    cantidad_agua = models.FloatField()  # Cantidad de agua utilizada (litros)

    def __str__(self):
        # Retorna la duración del riego
        return self.duracion

# Modelo de mantenimiento
class mantenimiento(models.Model):
    # Campos de mantenimiento
    fecha = models.DateField()  # Fecha de mantenimiento
    descripcion = models.CharField(max_length=200)  # Descripción de la actividad
    tipo = models.CharField(max_length=50)  # Tipo de mantenimiento

    def __str__(self):
        # Retorna la descripción del mantenimiento
        return self.descripcion