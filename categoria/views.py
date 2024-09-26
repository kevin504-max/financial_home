from django.shortcuts import render, get_object_or_404, redirect
from .models import Categoria
from .forms import CategoriaForm
from django.core.paginator import Paginator


def categoria_create(request):
    if request.method == 'POST':
        form = CategoriaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('categorias')  
    else:
        form = CategoriaForm()
    return render(request, 'categoria/categoria_form.html', {'form': form})

def categoria_list(request):
    categorias = Categoria.objects.all()
    paginator = Paginator(categorias, 6)  
    page_number = request.GET.get('page')
    categorias_paginated = paginator.get_page(page_number)
    return render(request, 'categoria/categorias.html', {'categorias': categorias_paginated})

def categoria_update(request, pk):
    categoria = get_object_or_404(Categoria, pk=pk)
    if request.method == 'POST':
        form = CategoriaForm(request.POST, instance=categoria)
        if form.is_valid():
            form.save()
            return redirect('categorias')  
    else:
        form = CategoriaForm(instance=categoria)
    return render(request, 'categoria/categoria_form.html', {'form': form})

def categoria_delete(request, pk):
    categoria = get_object_or_404(Categoria, pk=pk)
    if request.method == 'POST':
        categoria.delete()
        return redirect('categorias')
    return render(request, 'categoria/categoria_delete.html', {'categoria': categoria})
