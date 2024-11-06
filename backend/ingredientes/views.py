from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from .models import Ingrediente
from .serializers import IngredienteSerializer

@api_view(['GET', 'POST'])
def lista_ingredientes(request):
    if request.method == 'GET':
        ingredientes = Ingrediente.objects.all()
        serializer = IngredienteSerializer(ingredientes, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = IngredienteSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def detalle_ingrediente(request, id):
    try:
        ingrediente = Ingrediente.objects.get(id=id)
    except Ingrediente.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = IngredienteSerializer(ingrediente)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = IngredienteSerializer(ingrediente, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        ingrediente.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
@api_view(['POST'])
@permission_classes([IsAuthenticated])  # Cambia a AllowAny si es necesario
def agregar_ingrediente(request):
    serializer = IngredienteSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=201)
    return Response(serializer.errors, status=400)
