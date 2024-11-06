from rest_framework import serializers
from .models import Receta
from ingredientes.models import Ingrediente

class RecetaSerializer(serializers.ModelSerializer):
    ingredientes = serializers.PrimaryKeyRelatedField(queryset=Ingrediente.objects.all(), many=True)

    class Meta:
        model = Receta
        fields = ['id', 'nombre', 'descripcion', 'ingredientes', 'instrucciones', 'tiempo_preparacion']

    def create(self, validated_data):
        ingredientes_data = validated_data.pop('ingredientes')
        receta = Receta.objects.create(**validated_data)
        receta.ingredientes.set(ingredientes_data)
        return receta
