import uuid
from django.test import TestCase
from model_mommy import mommy

from core.models import get_file_name, Servico, Funcionario, Cargo

class GetFileNameTestCase(TestCase):
    def setUp(self):
        self.filename = 'teste.jpg'

    def test_get_file_name(self):
        result = get_file_name(None, self.filename)
        self.assertTrue(len(result), len(self.filename))
    

class ServicoTestCase(TestCase):
    
    def setUp(self):
        self.servico = mommy.make('Servico')

    def test_servico_str(self):
        self.assertEqual(str(self.servico), self.servico.servico)

class FuncionarioTestCase(TestCase):
    
    def setUp(self):
        self.cargo = mommy.make('Cargo')
        self.funcionario = mommy.make('Funcionario', cargo=self.cargo)
    
    def test_funcionario_str(self):
        self.assertEqual(str(self.funcionario), self.funcionario.nome)

class CargoTestCase(TestCase):
    
    def setUp(self):
        self.cargo = mommy.make('Cargo')

    def test_cargo_str(self):
        self.assertEqual(str(self.cargo), self.cargo.cargo)