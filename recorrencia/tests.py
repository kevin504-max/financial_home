# tests.py

from django.test import TestCase
from django.urls import reverse
from .models import Recorrencia
from .forms import RecorrenciaForm

class RecorrenciaViewsTest(TestCase):
    def setUp(self):
        # Criação de uma recorrência para testes
        self.recorrencia = Recorrencia.objects.create(nome='Teste Recorrencia')
        print(f'\n>>> Recorrência criada: {self.recorrencia.nome}')

    def test_recorrencia_create(self):
        print('\n======================================================================================================================')
        print('\n>>> Iniciando testes de views de recorrências...')        
        print('\n======================================================================================================================')
        print('\n>>> Testando a criação de uma nova recorrência...')
        response = self.client.post(reverse('recorrencia_create'), {'nome': 'Nova Recorrencia'})
        self.assertEqual(response.status_code, 302)  # Redireciona após criar
        print('\n>>> Redirecionamento após criação de recorrência confirmado')
        self.assertTrue(Recorrencia.objects.filter(nome='Nova Recorrencia').exists())
        print('\n>>> Nova recorrência criada com sucesso')

    def test_recorrencia_list(self):
        print('\n>>> Testando a listagem de recorrências...')
        response = self.client.get(reverse('recorrencias'))
        self.assertEqual(response.status_code, 200)
        print('\n>>> Listagem de recorrências retornou status 200')
        self.assertContains(response, 'Teste Recorrencia')
        print('\n>>> Recorrência de teste encontrada na listagem')

    def test_recorrencia_update(self):
        print('\n>>> Testando a atualização de uma recorrência...')
        response = self.client.post(reverse('recorrencia_update', args=[self.recorrencia.pk]), {'nome': 'Recorrencia Atualizada'})
        self.assertEqual(response.status_code, 302)  # Redireciona após atualizar
        print('\n>>> Redirecionamento após atualização de recorrência confirmado')
        self.recorrencia.refresh_from_db()
        self.assertEqual(self.recorrencia.nome, 'Recorrencia Atualizada')
        print('\n>>> Recorrência atualizada com sucesso')

    def test_recorrencia_delete(self):
        print('\n>>> Testando a exclusão de uma recorrência...')
        response = self.client.post(reverse('recorrencia_delete', args=[self.recorrencia.pk]))
        self.assertEqual(response.status_code, 302)  # Redireciona após deletar
        print('\n>>> Redirecionamento após exclusão de recorrência confirmado')
        self.assertFalse(Recorrencia.objects.filter(pk=self.recorrencia.pk).exists())
        print('\n>>> Recorrência excluída com sucesso')
