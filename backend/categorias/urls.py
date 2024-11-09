from django.urls import path
from .views import lista_categorias, crear_categoria, detalle_categoria, get_categorias

urlpatterns = [
    path('', lista_categorias, name='lista_categorias'),  # Para listar categorías
    path('crear/', crear_categoria, name='crear_categoria'),  # Para crear categorías
    path('<int:pk>/', detalle_categoria, name='detalle_categoria'),  # Para obtener detalles de una categoría
    path('api/', get_categorias, name='get_categorias'),  # Para obtener todas las categorías (pública)
]
