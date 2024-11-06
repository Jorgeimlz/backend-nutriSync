from django.urls import path
from .views import listar_planes, agregar_plan, detalle_plan, editar_plan, eliminar_plan

urlpatterns = [
    path('', listar_planes, name='listar_planes'),
    path('agregar/', agregar_plan, name='agregar_plan'),
    path('<int:plan_id>/', detalle_plan, name='detalle_plan'),
    path('<int:plan_id>/editar/', editar_plan, name='editar_plan'),
    path('<int:plan_id>/eliminar/', eliminar_plan, name='eliminar_plan'),
]
