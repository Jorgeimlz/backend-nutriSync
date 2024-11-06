# dieta/views.py

from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from .models import Dieta
from .serializers import DietaSerializer

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def lista_dietas(request):
    """Listar todas las dietas."""
    dietas = Dieta.objects.all()
    serializer = DietaSerializer(dietas, many=True)
    return Response(serializer.data)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def agregar_dieta(request):
    """Agregar una nueva dieta."""
    serializer = DietaSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=201)
    return Response(serializer.errors, status=400)
