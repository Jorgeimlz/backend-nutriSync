from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from .models import PlanAlimenticio
from .serializers import PlanAlimenticioSerializer

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def listar_planes(request):
    """Listar todos los planes alimenticios."""
    planes = PlanAlimenticio.objects.filter(usuario=request.user)  # Solo mostrar los planes del usuario
    serializer = PlanAlimenticioSerializer(planes, many=True)
    return Response(serializer.data)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def agregar_plan(request):
    """Agregar un nuevo plan alimenticio."""
    data = request.data.copy()
    data['usuario'] = request.user.id  # Asigna el usuario autenticado

    serializer = PlanAlimenticioSerializer(data=data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def detalle_plan(request, plan_id):
    """Obtener detalles de un plan alimenticio específico."""
    try:
        plan = PlanAlimenticio.objects.get(id=plan_id, usuario=request.user)  # Solo permitir el acceso si es el propietario
    except PlanAlimenticio.DoesNotExist:
        return Response({"error": "Plan no encontrado."}, status=404)

    serializer = PlanAlimenticioSerializer(plan)
    return Response(serializer.data)

@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def editar_plan(request, plan_id):
    """Editar un plan alimenticio existente."""
    try:
        plan = PlanAlimenticio.objects.get(id=plan_id, usuario=request.user)  # Solo permitir el acceso si es el propietario
    except PlanAlimenticio.DoesNotExist:
        return Response({"error": "Plan no encontrado."}, status=404)

    serializer = PlanAlimenticioSerializer(plan, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=400)

@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def eliminar_plan(request, plan_id):
    """Eliminar un plan alimenticio existente."""
    try:
        plan = PlanAlimenticio.objects.get(id=plan_id, usuario=request.user)  # Solo permitir el acceso si es el propietario
        plan.delete()
        return Response({"message": "Plan eliminado."}, status=204)
    except PlanAlimenticio.DoesNotExist:
        return Response({"error": "Plan no encontrado."}, status=404)
