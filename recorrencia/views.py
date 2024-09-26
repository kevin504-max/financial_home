from django.shortcuts import render, get_object_or_404, redirect

from .models import Recorrencia
from .forms import RecorrenciaForm
from django.core.paginator import Paginator

def recorrencia_create(request):
    if request.method == 'POST':
        form = RecorrenciaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('recorrencias') 
    else:
        form = RecorrenciaForm()
    return render(request, 'recorrencia/recorrencia_form.html', {'form': form})

def recorrencia_list(request):
    recorrencias = Recorrencia.objects.all().order_by('nome')
    paginator = Paginator(recorrencias, 6)  
    page_number = request.GET.get('page')
    recorrencias_paginated = paginator.get_page(page_number)

    return render(request, 'recorrencia/recorrencias.html', {'recorrencias': recorrencias_paginated})

def recorrencia_update(request, pk):
    recorrencia = get_object_or_404(Recorrencia, pk=pk)
    if request.method == 'POST':
        form = RecorrenciaForm(request.POST, instance=recorrencia)
        if form.is_valid():
            form.save()
            return redirect('recorrencias')
    else:
        form = RecorrenciaForm(instance=recorrencia)
    return render(request, 'recorrencia/recorrencia_form.html', {'form': form})

def recorrencia_delete(request, pk):
    recorrencia = get_object_or_404(Recorrencia, pk=pk)
    if request.method == 'POST':
        recorrencia.delete()
        return redirect('recorrencias')
    return render(request, 'recorrencia/recorrencia_delete.html', {'recorrencia': recorrencia})
