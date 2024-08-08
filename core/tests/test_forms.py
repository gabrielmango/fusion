from django.test import TestCase
from unittest.mock import patch
from .forms import ContatoForm

class ContatoFormTest(TestCase):

    def setUp(self):
        self.valid_form_data = {
            'nome': 'John Doe',
            'email': 'john@example.com',
            'assunto': 'Teste',
            'mensagem': 'Esta é uma mensagem de teste.'
        }
        self.invalid_form_data = {
            'nome': '',
            'email': '',
            'assunto': '',
            'mensagem': ''
        }

    def test_form_fields_required(self):
        form = ContatoForm(data=self.invalid_form_data)
        self.assertFalse(form.is_valid())
        self.assertIn('nome', form.errors)
        self.assertIn('email', form.errors)
        self.assertIn('assunto', form.errors)
        self.assertIn('mensagem', form.errors)

    @patch('django.core.mail.EmailMessage.send')
    def test_send_email(self, mock_send):
        form = ContatoForm(data=self.valid_form_data)
        self.assertTrue(form.is_valid())
        form.send_email()
        self.assertTrue(mock_send.called)

    @patch('django.core.mail.EmailMessage.send')
    def test_email_content(self, mock_send):
        form = ContatoForm(data=self.valid_form_data)
        self.assertTrue(form.is_valid())
        form.send_email()

        email_message = mock_send.call_args[0][0]
        self.assertIn('Contato - Fusion: Teste', email_message.subject)
        self.assertIn('Nome: John Doe', email_message.body)
        self.assertIn('Email: john@example.com', email_message.body)
        self.assertIn('Assunto: Teste', email_message.body)
        self.assertIn('Mensagem: Esta é uma mensagem de teste.', email_message.body)
