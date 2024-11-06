# dieta/models.py

from django.db import models

class Dieta(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    tipo = models.CharField(max_length=50)  # Ej: veganismo, vegetarianismo, etc.

    def __str__(self):
        return self.nombre
