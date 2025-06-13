from django import forms
from .models import Autor, Categoria, Entrada, Jugador, Torneo
from ckeditor.widgets import CKEditorWidget


class AutorForm(forms.ModelForm):
    class Meta:
        model = Autor
        fields = ['nombre', 'email']

class CategoriaForm(forms.ModelForm):
    class Meta:
        model = Categoria
        fields = ['nombre']

class EntradaForm(forms.ModelForm):
    class Meta:
        model = Entrada
        fields = ['titulo', 'imagen', 'contenido', 'autor', 'categoria', 'torneo']
        widgets = {
            'contenido': CKEditorWidget(),
        }

class BuscarEntradaForm(forms.Form):
    titulo = forms.CharField(max_length=200, required=False, label="Título")

class JugadorForm(forms.ModelForm):
    class Meta:
        model = Jugador
        fields = ['nombre', 'ranking', 'club', 'foto']

class TorneoForm(forms.ModelForm):
    class Meta:
        model = Torneo
        fields = ['nombre', 'fecha', 'lugar', 'jugadores', 'ganador', 'imagen']