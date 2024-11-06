# categorias/urls.py

from django.urls import path
from .views import lista_categorias, crear_categoria, detalle_categoria, get_categorias

urlpatterns = [
    path('', lista_categorias, name='lista_categorias'),
    path('crear/', crear_categoria, name='crear_categoria'),
    path('<int:pk>/', detalle_categoria, name='detalle_categoria'),
    path('api/categorias/', get_categorias, name='get_categorias'),
]
