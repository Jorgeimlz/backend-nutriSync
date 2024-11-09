# recetas/serializers.py
from rest_framework import serializers
from .models import Receta
from ingredientes.models import Ingrediente
from ingredientes.serializers import IngredienteSerializer

class RecetaSerializer(serializers.ModelSerializer):
    # Usa PrimaryKeyRelatedField para aceptar solo IDs en la entrada
    ingredientes = serializers.PrimaryKeyRelatedField(queryset=Ingrediente.objects.all(), many=True, required=False)

    # Incluye IngredienteSerializer para mostrar detalles completos en la salida
    ingredientes_detail = IngredienteSerializer(source='ingredientes', many=True, read_only=True)

    class Meta:
        model = Receta
        fields = ['id', 'nombre', 'descripcion', 'ingredientes', 'ingredientes_detail', 'instrucciones', 'tiempo_preparacion']
        extra_kwargs = {'ingredientes': {'write_only': True}}

    def create(self, validated_data):
        ingredientes_data = validated_data.pop('ingredientes', [])
        receta = Receta.objects.create(**validated_data)
        receta.ingredientes.set(ingredientes_data)
        return receta

    def update(self, instance, validated_data):
        ingredientes_data = validated_data.pop('ingredientes', [])
        instance.nombre = validated_data.get('nombre', instance.nombre)
        instance.descripcion = validated_data.get('descripcion', instance.descripcion)
        instance.instrucciones = validated_data.get('instrucciones', instance.instrucciones)
        instance.tiempo_preparacion = validated_data.get('tiempo_preparacion', instance.tiempo_preparacion)
        instance.save()
        
        # Actualiza la relación con ingredientes (acepta lista vacía)
        instance.ingredientes.set(ingredientes_data)
        
        return instance
