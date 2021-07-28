from django.db import models

# Create your models here.



class Servicios(models.Model):
    descripcion = models.CharField(max_length=100, null= True)
    precio = models.FloatField()

    def __str__(self):
        return self.descripcion

class Clientes(models.Model):
    NombreyApellido= models.CharField(max_length=30)
    DNI= models.CharField(max_length=8)
    direccion= models.CharField(max_length=20)

class Tecnicos(models.Model):
    NombreyApellido= models.CharField(max_length=30)
    DNI= models.CharField(max_length=8)
    direccion= models.CharField(max_length=20)