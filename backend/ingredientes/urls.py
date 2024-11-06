from django.urls import path
from .views import lista_ingredientes, detalle_ingrediente, agregar_ingrediente

urlpatterns = [
    path('api/ingredientes/', lista_ingredientes, name='lista_ingredientes'),
    path('api/ingredientes/<int:id>/', detalle_ingrediente, name='detalle_ingrediente'),
    path('api/ingredientes/agregar/', agregar_ingrediente, name='agregar_ingrediente'),
]
