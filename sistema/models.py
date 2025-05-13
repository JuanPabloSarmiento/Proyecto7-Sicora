from django.db import models

class usuario(models.Model):
    
    nombre = models.CharField(max_length=50)
    correo = models.EmailField(max_length=100)
    contraseña = models.CharField(max_length=100)
    rol = models.CharField(max_length=50)
    def __str__(self):
        return self.nombre
    
class zona_riego(models.Model):
    
    nombre_zona = models.CharField(max_length=50)
    tipo_planta = models.CharField(max_length=50)
    necesidades_hidricas = models.CharField(max_length=100)
    exposicion_solar = models.CharField(max_length=50)
    def __str__(self):
        return self.nombre_zona

class sensor(models.Model):
    
    tipo = models.CharField(max_length=50)
    estado = models.BooleanField()
    def __str__(self):
        return self.tipo
    


class configuracion_riego(models.Model):
    
    frecuencia = models.TimeField()
    hora_inicio = models.TimeField()
    duracion = models.TimeField()
    tipo_de_riego = models.CharField(max_length=50)
    caudal = models.FloatField()
    presion = models.FloatField()
    def __str__(self):
        return self.frecuencia

class lectura_sensor(models.Model):
    
    fecha_hora = models.DateField()
    valor = models.FloatField()
    def __str__(self):
        return self.valor
    

class historial_riego(models.Model):
    
    fecha = models.DateField()
    duracion = models.TimeField()
    cantidad_de_agua = models.FloatField()
    def __str__(self):
        return self.duracion

class mantenimiento(models.Model):
    
    fecha = models.DateField()
    descripcion = models.CharField(max_length=200)
    tipo = models.CharField(max_length=50)
    def __str__(self):
        return self.descripcion
    



