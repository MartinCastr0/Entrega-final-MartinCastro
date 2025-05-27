from django.shortcuts import render, redirect
from .models import Autor, Categoria, Entrada
from .forms import AutorForm, CategoriaForm, EntradaForm, BuscarEntradaForm

def index(request):
    return render(request, 'blog/index.html')

def crear_autor(request):
    if request.method == 'POST':
        form = AutorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = AutorForm()
    return render(request, 'blog/crear_autor.html', {'form': form})

def crear_categoria(request):
    if request.method == 'POST':
        form = CategoriaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = CategoriaForm()
    return render(request, 'blog/crear_categoria.html', {'form': form})

def crear_entrada(request):
    if request.method == 'POST':
        form = EntradaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = EntradaForm()
    return render(request, 'blog/crear_entrada.html', {'form': form})

def buscar_entrada(request):
    entradas = []
    if request.method == 'POST':
        form = BuscarEntradaForm(request.POST)
        if form.is_valid():
            titulo = form.cleaned_data['titulo']
            entradas = Entrada.objects.filter(titulo__icontains=titulo)
    else:
        form = BuscarEntradaForm()
    return render(request, 'blog/buscar_entrada.html', {'form': form, 'entradas': entradas})