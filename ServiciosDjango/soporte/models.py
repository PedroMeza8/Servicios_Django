from django.db import models

# Create your models here.



class Servicios(models.Model):
    descripcion = models.CharField(max_length=100, null= True)
    precio = models.FloatField()

    def __str__(self):
        return self.descripcion