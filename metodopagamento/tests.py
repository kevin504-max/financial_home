# tests.py

from django.test import TestCase
from django.urls import reverse
from .models import MetodoPagamento
from .forms import MetodoPagamentoForm

class MetodoPagamentoViewsTest(TestCase):
    def setUp(self):
        # Criação de um método de pagamento para testes
        self.metodo_pagamento = MetodoPagamento.objects.create(nome='Teste Metodo Pagamento')

    def test_metodo_pagamento_create(self):
        print('\n======================================================================================================================')
        print('\n>>> Iniciando testes de views de métodos de pagamento...')
        print('\n======================================================================================================================')
        print('\n>>> Testando a criação de um novo método de pagamento...')
        response = self.client.post(reverse('metodo_pagamento_create'), {'nome': 'Novo Metodo Pagamento'})
        self.assertEqual(response.status_code, 302)  # Redireciona após criar
        print('\n>>> Redirecionamento após criação de método de pagamento confirmado')
        self.assertTrue(MetodoPagamento.objects.filter(nome='Novo Metodo Pagamento').exists())
        print('\n>>> Novo método de pagamento criado com sucesso')

    def test_metodo_pagamento_list(self):
        print('\n>>> Testando a listagem de métodos de pagamento...')
        response = self.client.get(reverse('metodos_pagamento'))
        self.assertEqual(response.status_code, 200)
        print('\n>>> Listagem de métodos de pagamento retornou status 200')
        self.assertContains(response, 'Teste Metodo Pagamento')
        print('\n>>> Método de pagamento de teste encontrado na listagem')

    def test_metodo_pagamento_update(self):
        print('\n>>> Testando a atualização de um método de pagamento...')
        response = self.client.post(reverse('metodo_pagamento_update', args=[self.metodo_pagamento.pk]), {'nome': 'Metodo Atualizado'})
        self.assertEqual(response.status_code, 302)  # Redireciona após atualizar
        print('\n>>> Redirecionamento após atualização de método de pagamento confirmado')
        self.metodo_pagamento.refresh_from_db()
        self.assertEqual(self.metodo_pagamento.nome, 'Metodo Atualizado')
        print('\n>>> Método de pagamento atualizado com sucesso')

    def test_metodo_pagamento_delete(self):
        print('\n>>> Testando a exclusão de um método de pagamento...')
        response = self.client.post(reverse('metodo_pagamento_delete', args=[self.metodo_pagamento.pk]))
        self.assertEqual(response.status_code, 302)  # Redireciona após deletar
        print('\n>>> Redirecionamento após exclusão de método de pagamento confirmado')
        self.assertFalse(MetodoPagamento.objects.filter(pk=self.metodo_pagamento.pk).exists())
        print('\n>>> Método de pagamento excluído com sucesso')
