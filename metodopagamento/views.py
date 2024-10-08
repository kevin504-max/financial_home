import csv
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect

from .models import MetodoPagamento
from .forms import MetodoPagamentoForm
from django.core.paginator import Paginator

def exportar_csv(request):
    # Cria a resposta HTTP com o cabeçalho correto
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="Relação_de_Métodos_de_Pagamentos.csv"'

    writer = csv.writer(response)
    writer.writerow(['Nome'])

    metodos_pagamentos = MetodoPagamento.objects.all()
    for metodos_pagamento in metodos_pagamentos:
        writer.writerow([
            metodos_pagamento.nome,
        ])

    return response

def metodo_pagamento_list(request):
    metodos_pagamento = MetodoPagamento.objects.all().order_by('nome')
    paginator = Paginator(metodos_pagamento, 6)  
    page_number = request.GET.get('page')
    metodos_pagamento_paginated = paginator.get_page(page_number)
    return render(request, 'metodopagamento/metodos_pagamento.html', {'metodos_pagamento': metodos_pagamento_paginated})

def metodo_pagamento_create(request):
    if request.method == 'POST':
        form = MetodoPagamentoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('metodos_pagamento')
    else:
        form = MetodoPagamentoForm()
    return render(request, 'metodopagamento/metodos_pagamento_form.html', {'form': form})

def metodo_pagamento_update(request, pk):
    metodo_pagamento = get_object_or_404(MetodoPagamento, pk=pk)
    if request.method == 'POST':
        form = MetodoPagamentoForm(request.POST, instance=metodo_pagamento)
        if form.is_valid():
            form.save()
            return redirect('metodos_pagamento')
    else:
        form = MetodoPagamentoForm(instance=metodo_pagamento)
    return render(request, 'metodopagamento/metodos_pagamento_form.html', {'form': form})

def metodo_pagamento_delete(request, pk):
    metodo_pagamento = get_object_or_404(MetodoPagamento, pk=pk)
    if request.method == 'POST':
        metodo_pagamento.delete()
        return redirect('metodos_pagamento')
    return render(request, 'metodopagamento/metodos_pagamento_delete.html', {'metodo_pagamento': metodo_pagamento})
