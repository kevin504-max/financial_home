import csv
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from .models import Gastos
from .forms import GastosForm
from .factory.gasto_factory import GastoFactory
from .singleton.gasto_totalizador import GastoTotalizador
from categoria.models import Categoria
from metodopagamento.models import MetodoPagamento
from recorrencia.models import Recorrencia 
from usuarios.models import Usuario
from utilitarios.filtros import formatar_dinheiro

def exportar_csv(request):
    # Cria a resposta HTTP com o cabeçalho correto
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="Relação_de_Gastos.csv"'

    writer = csv.writer(response)
    writer.writerow(['Descrição', 'Valor', 'Data', 'Categoria', 'Método de Pagamento', 'Recorrência', 'Usuário'])

    gastos = Gastos.objects.all()
    for gasto in gastos:
        writer.writerow([
            gasto.descricao,
            gasto.valor,
            gasto.data,
            gasto.categoria.nome,
            gasto.metodo_pagamento.nome,
            gasto.recorrencia.nome,
            gasto.usuario.nome
        ])

    return response

def home(request):
    return render(request, 'home.html')

def gastos_create(request):
    form = GastosForm(request.POST or None)
    
    if form.is_valid():
        dados = form.cleaned_data
        print('dados: ', dados)
        novo_gasto = GastoFactory.criar_gasto(**dados)
        novo_gasto.save()

        return redirect('gastos')
    
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
    for gasto in gastos:
        gasto.valor_formatado = formatar_dinheiro(gasto.valor)
    totalizador = GastoTotalizador()
    total = totalizador.calcular_total(gastos)

    contexto = {
        'categorias': Categoria.objects.all(),
        'metodos_pagamento': MetodoPagamento.objects.all(),
        'recorrencias': Recorrencia.objects.all(),
        'usuarios': Usuario.objects.all(),
    }

    return render(request, 'financas/gastos.html', {'gastos': gastos, 'total': total, 'contexto': contexto})

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
