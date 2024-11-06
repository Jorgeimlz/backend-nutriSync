from django.db import models
from ingredientes.models import Ingrediente  # Asegúrate de que este modelo existe

class Receta(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    ingredientes = models.ManyToManyField(Ingrediente)  # Relación con Ingrediente
    instrucciones = models.TextField()
    tiempo_preparacion = models.IntegerField()  # Tiempo en minutos

    def __str__(self):
        return self.nombre
