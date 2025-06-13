from django import forms
from .models import Autor, Categoria, Entrada, Jugador, Torneo

class AutorForm(forms.ModelForm):
    class Meta:
        model = Autor
        fields = '__all__'

class CategoriaForm(forms.ModelForm):
    class Meta:
        model = Categoria
        fields = '__all__'

class EntradaForm(forms.ModelForm):
    class Meta:
        model = Entrada
        fields = '__all__'

class BuscarEntradaForm(forms.Form):
    titulo = forms.CharField(label='Título', max_length=200, required=False)

class JugadorForm(forms.ModelForm):
    class Meta:
        model = Jugador
        fields = '__all__'

class TorneoForm(forms.ModelForm):
    class Meta:
        model = Torneo
        fields = '__all__'
        widgets = {
            'fecha': forms.DateInput(attrs={'type': 'date'}),
        }