from django.db import models

# Create your models here.

class Familiar(models.Model):
    nombre = models.CharField(max_length=100)
    direccion = models.CharField(max_length=200)
    numero_pasaporte = models.IntegerField()
    fec_nacimiento = models.DateField(null=True)
def __str__(self):
    # return f"{self.nombre}, {self.numero_pasaporte}, {self.id}, {self.fec_nacimiento}"
    return f"{self.nombre}, {self.numero_pasaporte}, {self.id}, {self.fec_nacimiento}"


class Vehiculo(models.Model):
    marca = models.CharField(max_length=100)
    modelo = models.CharField(max_length=100)
    patente = models.CharField(max_length=10)
    kms = models.IntegerField(10)


class Mascota(models.Model):
    especie = models.CharField(max_length=50)
    nombre = models.CharField(max_length=50)
    raza = models.CharField(max_length=50)
    
    
    