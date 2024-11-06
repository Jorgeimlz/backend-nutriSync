# serializers.py en planes_alimenticios
from rest_framework import serializers
from .models import PlanAlimenticio

class PlanAlimenticioSerializer(serializers.ModelSerializer):
    class Meta:
        model = PlanAlimenticio
        fields = ['id', 'usuario', 'dieta', 'nombre', 'descripcion', 'fecha_inicio']  # Asegúrate de que todos los campos estén aquí

    def create(self, validated_data):
        return PlanAlimenticio.objects.create(**validated_data)
