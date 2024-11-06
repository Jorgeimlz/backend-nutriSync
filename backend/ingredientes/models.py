from django.db import models
from categorias.models import Categoria

class Ingrediente(models.Model):
    nombre = models.CharField(max_length=100)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    cantidad_disponible = models.PositiveIntegerField()
    unidad_medida = models.CharField(max_length=50)
    descripcion = models.TextField(blank=True)

    def __str__(self):
        return self.nombre
