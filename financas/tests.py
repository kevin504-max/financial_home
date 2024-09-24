# tests.py

from django.test import TestCase
from django.urls import reverse
from .models import Gastos
from .forms import GastosForm
from .factory.gasto_factory import GastoFactory
from .singleton.gasto_totalizador import GastoTotalizador
from categoria.models import Categoria
from metodopagamento.models import MetodoPagamento
from recorrencia.models import Recorrencia
from usuarios.models import Usuario
from datetime import date

class GastosViewsTest(TestCase):
    def setUp(self):
        # Criação de instâncias necessárias para os testes
        self.categoria = Categoria.objects.create(nome='Teste Categoria')
        self.metodo_pagamento = MetodoPagamento.objects.create(nome='Teste Metodo Pagamento')
        self.recorrencia = Recorrencia.objects.create(nome='Teste Recorrencia')
        self.usuario = Usuario.objects.create(nome='Teste Usuario', email='teste@usuario.com')
        self.gasto = Gastos.objects.create(
            descricao='Teste Gasto',
            valor=100.00,
            categoria=self.categoria,
            metodo_pagamento=self.metodo_pagamento,
            recorrencia=self.recorrencia,
            usuario=self.usuario,
            data=date.today()  # Adicionando a data
        )

    def test_gastos_create(self):
        print('\n======================================================================================================================')
        print('\n>>> Iniciando testes de views de gastos...')        
        print('\n======================================================================================================================')
        print('\n>>> Testando a criação de um novo gasto...')
        
        # Usando o padrão Factory para criar um novo gasto
        response = self.client.post(reverse('gastos_create'), {
            'descricao': 'Novo Gasto',
            'valor': 200.00,
            'categoria': self.categoria.pk,
            'metodo_pagamento': self.metodo_pagamento.pk,
            'recorrencia': self.recorrencia.pk,
            'usuario': self.usuario.pk,
            'data': date.today()  # Adicionando a data
        })
        
        self.assertEqual(response.status_code, 302)  # Redireciona após criar
        print('\n>>> Redirecionamento após criação de gasto confirmado')
        
        # Verificando se o novo gasto foi criado com sucesso
        self.assertTrue(Gastos.objects.filter(descricao='Novo Gasto').exists())
        print('\n>>> Novo gasto criado com sucesso')

        # Explicação sobre o uso do padrão Factory
        print('\n>>> O padrão Factory é utilizado aqui para abstrair a lógica de criação de objetos.')
        print('>>> Ao invés de criar diretamente uma instância de Gastos, utilizamos o GastoFactory para encapsular')
        print('>>> essa lógica, o que nos permite criar gastos de forma mais flexível e reutilizável.')

    def test_gastos_list(self):
        print('\n>>> Testando a listagem de gastos...')
        response = self.client.get(reverse('gastos'))
        self.assertEqual(response.status_code, 200)
        print('\n>>> Listagem de gastos retornou status 200')
        self.assertContains(response, 'Teste Gasto')
        print('\n>>> Gasto de teste encontrado na listagem')

    def test_gastos_update(self):
        print('\n>>> Testando a atualização de um gasto...')
        response = self.client.post(reverse('gastos_update', args=[self.gasto.pk]), {
            'descricao': 'Gasto Atualizado',
            'valor': 150.00,
            'categoria': self.categoria.pk,
            'metodo_pagamento': self.metodo_pagamento.pk,
            'recorrencia': self.recorrencia.pk,
            'usuario': self.usuario.pk,
            'data': date.today()  # Adicionando a data
        })
        self.assertEqual(response.status_code, 302)  # Redireciona após atualizar
        print('\n>>> Redirecionamento após atualização de gasto confirmado')
        self.gasto.refresh_from_db()
        self.assertEqual(self.gasto.descricao, 'Gasto Atualizado')
        print('\n>>> Gasto atualizado com sucesso')

    def test_gastos_delete(self):
        print('\n>>> Testando a exclusão de um gasto...')
        response = self.client.post(reverse('gastos_delete', args=[self.gasto.pk]))
        self.assertEqual(response.status_code, 302)  # Redireciona após deletar
        print('\n>>> Redirecionamento após exclusão de gasto confirmado')
        self.assertFalse(Gastos.objects.filter(pk=self.gasto.pk).exists())
        print('\n>>> Gasto excluído com sucesso')
