# recetas/urls.py
from django.urls import path
from .views import (
    lista_recetas,
    agregar_receta,
    detalle_receta,
    editar_receta,
    eliminar_receta,
    obtener_ingredientes
)

urlpatterns = [
    path('', lista_recetas, name='lista_recetas'),  # Listar todas las recetas
    path('agregar/', agregar_receta, name='agregar_receta'),  # Agregar nueva receta
    path('ingredientes/', obtener_ingredientes, name='obtener_ingredientes'),  # Obtener ingredientes
    path('<int:receta_id>/', detalle_receta, name='detalle_receta'),  # Obtener detalles de una receta
    path('<int:receta_id>/editar/', editar_receta, name='editar_receta'),  # Editar receta
    path('<int:receta_id>/eliminar/', eliminar_receta, name='eliminar_receta'),  # Eliminar receta
]

