import csv
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from .models import Categoria
from .forms import CategoriaForm
from django.core.paginator import Paginator


def exportar_csv(request):
    # Cria a resposta HTTP com o cabeçalho correto
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="Relação_de_Categorias.csv"'

    writer = csv.writer(response)
    writer.writerow(['Nome'])

    categorias = Categoria.objects.all()
    for categoria in categorias:
        writer.writerow([
            categoria.nome,
        ])

    return response

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
    categorias = Categoria.objects.all().order_by('nome')
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
