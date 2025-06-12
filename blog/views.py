from django.shortcuts import render, redirect, get_object_or_404
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

# === VISTAS CRUD para pages (Entrada) ===

def pages_list(request):
    pages = Entrada.objects.all()
    return render(request, 'blog/pages/pages_list.html', {'pages': pages})

def page_detail(request, pk):
    page = get_object_or_404(Entrada, pk=pk)
    return render(request, 'blog/pages/page_detail.html', {'page': page})

def page_create(request):
    if request.method == 'POST':
        form = EntradaForm(request.POST)
        if form.is_valid():
            page = form.save()
            return redirect('page_detail', pk=page.pk)
    else:
        form = EntradaForm()
    return render(request, 'blog/pages/page_form.html', {'form': form, 'page': None})

def page_update(request, pk):
    page = get_object_or_404(Entrada, pk=pk)
    if request.method == 'POST':
        form = EntradaForm(request.POST, instance=page)
        if form.is_valid():
            form.save()
            return redirect('page_detail', pk=page.pk)
    else:
        form = EntradaForm(instance=page)
    return render(request, 'blog/pages/page_form.html', {'form': form, 'page': page})

def page_delete(request, pk):
    page = get_object_or_404(Entrada, pk=pk)
    if request.method == 'POST':
        page.delete()
        return redirect('pages_list')
    return render(request, 'blog/pages/page_confirm_delete.html', {'page': page})

# === VISTAS EXTRA PARA ENTRADAS ===

def editar_entrada(request, pk):
    entrada = get_object_or_404(Entrada, pk=pk)
    if request.method == 'POST':
        form = EntradaForm(request.POST, instance=entrada)
        if form.is_valid():
            form.save()
            return redirect('pages_list')
    else:
        form = EntradaForm(instance=entrada)
    return render(request, 'blog/crear_entrada.html', {'form': form, 'entrada': entrada})

def borrar_entrada(request, pk):
    entrada = get_object_or_404(Entrada, pk=pk)
    if request.method == 'POST':
        entrada.delete()
        return redirect('pages_list')
    return render(request, 'blog/pages/page_confirm_delete.html', {'page': entrada})