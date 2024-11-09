# recetas/models.py
from django.db import models
from ingredientes.models import Ingrediente

class Receta(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    instrucciones = models.TextField()
    tiempo_preparacion = models.IntegerField()

    # Relación muchos a muchos con ingredientes
    ingredientes = models.ManyToManyField(Ingrediente, through='IngredientesRecetas')

    def __str__(self):
        return self.nombre

class IngredientesRecetas(models.Model):
    receta = models.ForeignKey(Receta, on_delete=models.CASCADE)
    ingrediente = models.ForeignKey(Ingrediente, on_delete=models.CASCADE)
    
    def __str__(self):
        return f'{self.ingrediente.nombre} en {self.receta.nombre}'
