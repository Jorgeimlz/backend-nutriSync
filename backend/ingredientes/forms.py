from django import forms
from .models import Ingrediente

class IngredienteForm(forms.ModelForm):
    class Meta:
        model = Ingrediente
        fields = ['nombre', 'categoria', 'cantidad_disponible', 'unidad_medida']
