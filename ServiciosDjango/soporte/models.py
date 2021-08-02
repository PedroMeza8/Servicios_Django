from django.db import models

# Create your models here.



class Servicios(models.Model):
    descripcion = models.CharField(max_length=30, null= True)
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

class Movimientos(models.Model):
    lista=[('pendiente','pendiente'), ('finalizado', 'finalizado')]
    cliente= models.ForeignKey(Clientes, on_delete=models.CASCADE)
    servicio= models.ForeignKey(Servicios, on_delete=models.CASCADE)
    tecnico= models.ForeignKey(Tecnicos, on_delete=models.CASCADE)
    estado= models.CharField(max_length=20, choices=lista, null=True)     