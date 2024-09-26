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
from django.core.paginator import Paginator


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


def gastos_list(request):
    mes = request.GET.get('mes')
    ano = request.GET.get('ano')
    recorrencia = request.GET.get('recorrencia')
    categoria = request.GET.get('categoria')
    gastosAll = Gastos.objects.all()
    
    filtros = {}

    if mes:
        filtros['data__month'] = mes
    if ano:
        filtros['data__year'] = ano
    if recorrencia:
        filtros['recorrencia_id'] = recorrencia
    if categoria:
        filtros['categoria_id'] = categoria
    
    gastos = Gastos.objects.filter(**filtros).order_by('-data')
    
    for gasto in gastos:
        gasto.valor_formatado = formatar_dinheiro(gasto.valor)

    meses = [
        (1, 'Janeiro'),
        (2, 'Fevereiro'),
        (3, 'Março'),
        (4, 'Abril'),
        (5, 'Maio'),
        (6, 'Junho'),
        (7, 'Julho'),
        (8, 'Agosto'),
        (9, 'Setembro'),
        (10, 'Outubro'),
        (11, 'Novembro'),
        (12, 'Dezembro'),
    ]

    anos = gastosAll.dates('data', 'year')  
    
    totalizador = GastoTotalizador()
    total = totalizador.calcular_total(gastos)
    paginator = Paginator(gastos, 5)  
    page_number = request.GET.get('page')
    gastos_paginated = paginator.get_page(page_number)

    contexto = {
        'categorias': Categoria.objects.all(),
        'metodos_pagamento': MetodoPagamento.objects.all(),
        'recorrencias': Recorrencia.objects.all(),
        'usuarios': Usuario.objects.all(),
        'meses': meses,
        'anos': anos,
    }

    return render(request, 'financas/gastos.html', {'gastos': gastos_paginated, 'total': total, 'contexto': contexto})

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
