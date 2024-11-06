# ingredientes/serializers.py
from rest_framework import serializers
from .models import Ingrediente

class IngredienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ingrediente
        fields = ['id', 'nombre', 'cantidad_disponible', 'unidad_medida']
