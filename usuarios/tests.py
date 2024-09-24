# tests.py

from django.test import TestCase
from django.urls import reverse
from .models import Usuario
from .forms import UsuarioForm

class UsuarioViewsTest(TestCase):
    def setUp(self):
        # Criação de um usuário para testes
        self.usuario = Usuario.objects.create(nome='Teste Usuario', email='teste@usuario.com')
        print(f'\n>>> Usuário criado: {self.usuario.nome}')

    def test_usuario_create(self):
        print('\n======================================================================================================================')
        print('\n>>> Iniciando testes de views de usuários...')        
        print('\n======================================================================================================================')
        print('\n>>> Testando a criação de um novo usuário...')
        response = self.client.post(reverse('usuario_create'), {'nome': 'Novo Usuario', 'email': 'novo@usuario.com'})
        self.assertEqual(response.status_code, 302)  # Redireciona após criar
        print('\n>>> Redirecionamento após criação de usuário confirmado')
        self.assertTrue(Usuario.objects.filter(nome='Novo Usuario').exists())
        print('\n>>> Novo usuário criado com sucesso')

    def test_usuario_list(self):
        print('\n>>> Testando a listagem de usuários...')
        response = self.client.get(reverse('usuarios'))
        self.assertEqual(response.status_code, 200)
        print('\n>>> Listagem de usuários retornou status 200')
        self.assertContains(response, 'Teste Usuario')
        print('\n>>> Usuário de teste encontrado na listagem')

    def test_usuario_update(self):
        print('\n>>> Testando a atualização de um usuário...')
        response = self.client.post(reverse('usuario_update', args=[self.usuario.pk]), {'nome': 'Usuario Atualizado', 'email': 'atualizado@usuario.com'})
        self.assertEqual(response.status_code, 302)  # Redireciona após atualizar
        print('\n>>> Redirecionamento após atualização de usuário confirmado')
        self.usuario.refresh_from_db()
        self.assertEqual(self.usuario.nome, 'Usuario Atualizado')
        print('\n>>> Usuário atualizado com sucesso')

    def test_usuario_delete(self):
        print('\n>>> Testando a exclusão de um usuário...')
        response = self.client.post(reverse('usuario_delete', args=[self.usuario.pk]))
        self.assertEqual(response.status_code, 302)  # Redireciona após deletar
        print('\n>>> Redirecionamento após exclusão de usuário confirmado')
        self.assertFalse(Usuario.objects.filter(pk=self.usuario.pk).exists())
        print('\n>>> Usuário excluído com sucesso')
