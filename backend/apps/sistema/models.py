# Importa la clase base Model de Django para crear modelos de base de datos
from django.db import models

# Modelo de configuración de riego
class configuracion_riego(models.Model):
    # Campos de configuración
    frecuencia = models.TimeField()  # Frecuencia de riego
    hora_inicio = models.TimeField()  # Hora de inicio del riego
    duracion = models.TimeField()  # Duración del riego
    tipo_riego = models.CharField(max_length=50)  # Tipo de riego (goteo, aspersión, etc.)
    caudal = models.FloatField()  # Caudal de agua (litros/segundo)
    presion = models.FloatField()  # Presión de agua (bar)

    def __str__(self):
        # Retorna la frecuencia de riego
        return self.frecuencia
    
# Modelo de zona de riego
class zona_riego(models.Model):
    # Campos de la zona de riego
    nombre_zona = models.CharField(max_length=50)  # Nombre de la zona
    tipo_planta = models.CharField(max_length=50)  # Tipo de planta cultivada
    necesidades_hidricas = models.CharField(max_length=100)  # Necesidades de agua
    exposicion_solar = models.CharField(max_length=50)  # Nivel de exposición al sol

    def __str__(self):
        # Retorna el nombre de la zona
        return self.nombre_zona

# Modelo de sensor
class sensor(models.Model):
    # Campos del sensor
    tipo = models.CharField(max_length=50)  # Tipo de sensor
    estado = models.BooleanField()  # Estado del sensor (activo/inactivo)

    def __str__(self):
        # Retorna el tipo de sensor
        return self.tipo

# Modelo de lectura de sensor
class lectura_sensor(models.Model):
    fecha_hora = models.DateTimeField()  # Fecha y hora completa
    valor = models.FloatField()  # Valor registrado
    unidad = models.CharField(
        max_length=10,
        choices=[('porcentaje', 'Porcentaje'), ('grados', 'Grados')],
        default='porcentaje'
    )

    def __str__(self):
        simbolo = "%" if self.unidad == "porcentaje" else "°"
        return f"{self.valor}{simbolo} - {self.fecha_hora}"
    
# fin del archivo sistema/models.py
