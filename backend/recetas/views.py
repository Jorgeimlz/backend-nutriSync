# recetas/views.py
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
    """Listar todas las recetas en orden de las más nuevas a las más antiguas."""
    recetas = Receta.objects.all().order_by('-id')  # Ordena por ID descendente, las más nuevas primero
    serializer = RecetaSerializer(recetas, many=True)
    return Response(serializer.data)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def agregar_receta(request):
    """Agregar una nueva receta."""
    serializer = RecetaSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()  # Guarda la receta con sus ingredientes
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def obtener_ingredientes(request):
    """Obtener todos los ingredientes."""
    ingredientes = Ingrediente.objects.all()
    serializer = IngredienteSerializer(ingredientes, many=True)
    return Response(serializer.data)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def detalle_receta(request, receta_id):
    """Obtener detalles de una receta específica."""
    try:
        receta = Receta.objects.get(id=receta_id)
    except Receta.DoesNotExist:
        return Response({"error": "Receta no encontrada."}, status=status.HTTP_404_NOT_FOUND)

    serializer = RecetaSerializer(receta)
    return Response(serializer.data)

@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def editar_receta(request, receta_id):
    """Editar una receta existente."""
    try:
        receta = Receta.objects.get(id=receta_id)
    except Receta.DoesNotExist:
        return Response({"error": "Receta no encontrada."}, status=status.HTTP_404_NOT_FOUND)

    serializer = RecetaSerializer(receta, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def eliminar_receta(request, receta_id):
    """Eliminar una receta existente."""
    try:
        receta = Receta.objects.get(id=receta_id)
        receta.delete()
        return Response({"message": "Receta eliminada."}, status=status.HTTP_204_NO_CONTENT)
    except Receta.DoesNotExist:
        return Response({"error": "Receta no encontrada."}, status=status.HTTP_404_NOT_FOUND)
