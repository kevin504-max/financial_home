# tests.py

from django.test import TestCase
from django.urls import reverse
from .models import Categoria
from .forms import CategoriaForm

class CategoriaViewsTest(TestCase):
    def setUp(self):
        # Criação de uma categoria para testes
        self.categoria = Categoria.objects.create(nome='Teste Categoria')

    def test_categoria_create(self):
        print('\n======================================================================================================================')
        print('\n>>> Iniciando testes de views de categoria...')
        print('\n======================================================================================================================')
        print('\n>>> Testando a criação de uma nova categoria...')
        response = self.client.post(reverse('categoria_create'), {'nome': 'Nova Categoria'})
        self.assertEqual(response.status_code, 302)  # Redireciona após criar
        print('\n>>> Redirecionamento após criação de categoria confirmado')
        self.assertTrue(Categoria.objects.filter(nome='Nova Categoria').exists())
        print('\n>>> Nova categoria criada com sucesso')

    def test_categoria_list(self):
        print('\n>>> Testando a listagem de categorias...')
        response = self.client.get(reverse('categorias'))
        self.assertEqual(response.status_code, 200)
        print('\n>>> Listagem de categorias retornou status 200')
        self.assertContains(response, 'Teste Categoria')
        print('\n>>> Categoria de teste encontrada na listagem')

    def test_categoria_update(self):
        print('\n>>> Testando a atualização de uma categoria...')
        response = self.client.post(reverse('categoria_update', args=[self.categoria.pk]), {'nome': 'Categoria Atualizada'})
        self.assertEqual(response.status_code, 302)  # Redireciona após atualizar
        print('\n>>> Redirecionamento após atualização de categoria confirmado')
        self.categoria.refresh_from_db()
        self.assertEqual(self.categoria.nome, 'Categoria Atualizada')
        print('\n>>> Categoria atualizada com sucesso')

    def test_categoria_delete(self):
        print('\n>>> Testando a exclusão de uma categoria...')
        response = self.client.post(reverse('categoria_delete', args=[self.categoria.pk]))
        self.assertEqual(response.status_code, 302)  # Redireciona após deletar
        print('\n>>> Redirecionamento após exclusão de categoria confirmado')
        self.assertFalse(Categoria.objects.filter(pk=self.categoria.pk).exists())
        print('\n>>> Categoria excluída com sucesso')
