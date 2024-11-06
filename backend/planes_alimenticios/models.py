# models.py en planes_alimenticios
from django.db import models
from django.conf import settings
from dieta.models import Dieta  # Asegúrate de que este modelo existe

class PlanAlimenticio(models.Model):
    usuario = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    dieta = models.ForeignKey(Dieta, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=100)  # Este campo debe estar presente
    descripcion = models.TextField()
    fecha_inicio = models.DateField()
    
    def __str__(self):
        return self.nombre
