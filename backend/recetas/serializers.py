from rest_framework import serializers
from .models import Receta, IngredientesRecetas
from ingredientes.models import Ingrediente

class IngredienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ingrediente
        fields = ['id', 'nombre']

class IngredientesRecetasSerializer(serializers.ModelSerializer):
    class Meta:
        model = IngredientesRecetas
        fields = ['ingrediente', 'receta']

class RecetaSerializer(serializers.ModelSerializer):
    ingredientes = serializers.PrimaryKeyRelatedField(queryset=Ingrediente.objects.all(), many=True)

    class Meta:
        model = Receta
        fields = ['id', 'nombre', 'descripcion', 'ingredientes', 'instrucciones', 'tiempo_preparacion']

    def create(self, validated_data):
        ingredientes_data = validated_data.pop('ingredientes')
        receta = Receta.objects.create(**validated_data)
        for ingrediente in ingredientes_data:
            IngredientesRecetas.objects.create(receta=receta, ingrediente=ingrediente)
        return receta
