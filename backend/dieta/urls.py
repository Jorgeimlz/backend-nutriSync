# dieta/urls.py

from django.urls import path
from .views import lista_dietas, agregar_dieta

urlpatterns = [
    path('', lista_dietas, name='lista_dietas'),  # Para listar dietas
    path('agregar/', agregar_dieta, name='agregar_dieta'),  # Para agregar dieta

]
