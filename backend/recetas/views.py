from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from .models import Receta
from .serializers import RecetaSerializer
from ingredientes.models import Ingrediente
from ingredientes.serializers import IngredienteSerializer 
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def lista_recetas(request):
    """Listar todas las recetas."""
    recetas = Receta.objects.all()
    serializer = RecetaSerializer(recetas, many=True)
    return Response(serializer.data)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def agregar_receta(request):
    """Agregar una nueva receta."""
    serializer = RecetaSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=201)
    return Response(serializer.errors, status=400)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def obtener_ingredientes(request):
    """Obtener todos los ingredientes."""
    ingredientes = Ingrediente.objects.all()
    serializer = IngredienteSerializer(ingredientes, many=True)  # Asegúrate de usar el serializador correcto
    return Response(serializer.data)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def detalle_receta(request, receta_id):
    """Obtener detalles de una receta específica."""
    try:
        receta = Receta.objects.get(id=receta_id)
    except Receta.DoesNotExist:
        return Response({"error": "Receta no encontrada."}, status=404)

    serializer = RecetaSerializer(receta)
    return Response(serializer.data)

@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def editar_receta(request, receta_id):
    """Editar una receta existente."""
    try:
        receta = Receta.objects.get(id=receta_id)
    except Receta.DoesNotExist:
        return Response({"error": "Receta no encontrada."}, status=404)

    serializer = RecetaSerializer(receta, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=400)

@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def eliminar_receta(request, receta_id):
    """Eliminar una receta existente."""
    try:
        receta = Receta.objects.get(id=receta_id)
        receta.delete()
        return Response({"message": "Receta eliminada."}, status=204)
    except Receta.DoesNotExist:
        return Response({"error": "Receta no encontrada."}, status=404)
