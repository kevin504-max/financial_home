from django.shortcuts import render, get_object_or_404, redirect
from .models import Gastos
from .forms import GastosForm
from .factory.gasto_factory import GastoFactory
from .singleton.gasto_totalizador import GastoTotalizador
from categoria.models import Categoria
from metodopagamento.models import MetodoPagamento
from recorrencia.models import Recorrencia 
from usuarios.models import Usuario

def gastos_create(request):
    form = GastosForm(request.POST or None)
    
    if form.is_valid():
        dados = form.cleaned_data
        
        novo_gasto = GastoFactory.criar_gasto(**dados)
        novo_gasto.save()

        return redirect('gastos')
    else:
        form = GastosForm()

    contexto = {
        'form': form,
        'categorias': Categoria.objects.all(),
        'metodos_pagamento': MetodoPagamento.objects.all(),
        'recorrencias': Recorrencia.objects.all(),
        'usuarios': Usuario.objects.all(),
    }
    return render(request, 'financas/gasto_form.html', contexto)

# Read (List)
def gastos_list(request):
    gastos = Gastos.objects.all()
    totalizador = GastoTotalizador()
    total = totalizador.calcular_total(gastos)
    return render(request, 'financas/gastos.html', {'gastos': gastos, 'total': total})

# Update
def gastos_update(request, pk):
    gastos = get_object_or_404(Gastos, pk=pk)
    if request.method == 'POST':
        form = GastosForm(request.POST, instance=gastos)
        if form.is_valid():
            form.save()
            return redirect('gastos')
    else:
        form = GastosForm(instance=gastos)
    return render(request, 'financas/gasto_form.html', {'form': form})

# Delete
def gastos_delete(request, pk):
    gastos = get_object_or_404(Gastos, pk=pk)
    if request.method == 'POST':
        gastos.delete()
        return redirect('gastos')
    return render(request, 'financas/gasto_delete.html', {'gastos': gastos})
