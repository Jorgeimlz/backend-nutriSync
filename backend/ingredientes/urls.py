from django.urls import path
from .views import lista_ingredientes, detalle_ingrediente, agregar_ingrediente

urlpatterns = [
    path('', lista_ingredientes, name='lista_ingredientes'),  # Para listar ingredientes
    path('<int:id>/', detalle_ingrediente, name='detalle_ingrediente'),  # Para detalles de un ingrediente
    path('agregar/', agregar_ingrediente, name='agregar_ingrediente'),  # Para agregar un nuevo ingrediente
]
