from django.db import models
from ingredientes.models import Ingrediente

class Receta(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    instrucciones = models.TextField()
    tiempo_preparacion = models.IntegerField()  # Tiempo en minutos

    def __str__(self):
        return self.nombre


class IngredientesRecetas(models.Model):
    ingrediente = models.ForeignKey(Ingrediente, on_delete=models.CASCADE)
    receta = models.ForeignKey(Receta, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('ingrediente', 'receta')

    def __str__(self):
        return f"{self.ingrediente} en {self.receta}"
