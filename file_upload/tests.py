from django.test import TestCase, Client
from django.urls import reverse
from django.core.files.uploadedfile import SimpleUploadedFile
from django.contrib.auth.models import User
from .models import UploadedFile
import os
import tempfile

class FileUploadModelTest(TestCase):
    def setUp(self):
        self.test_file = SimpleUploadedFile(
            "test.txt",
            b"test file content",
            content_type="text/plain"
        )

    def test_uploaded_file_creation(self):
        """Testa a criação de um arquivo enviado"""
        file_obj = UploadedFile.objects.create(
            file=self.test_file,
            description="Test file"
        )
        
        self.assertEqual(file_obj.filename, "test.txt")
        self.assertEqual(file_obj.file_type, ".txt")
        self.assertEqual(file_obj.description, "Test file")
        self.assertIsNotNone(file_obj.uploaded_at)

    def test_file_size_calculation(self):
        """Testa o cálculo automático do tamanho do arquivo"""
        file_obj = UploadedFile.objects.create(file=self.test_file)
        self.assertEqual(file_obj.file_size, 17)  # "test file content" tem 17 bytes

    def test_string_representation(self):
        """Testa a representação em string do modelo"""
        file_obj = UploadedFile.objects.create(file=self.test_file)
        self.assertEqual(str(file_obj), "test.txt")

class FileUploadViewTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.upload_url = reverse('file_upload:home')
        self.test_file = SimpleUploadedFile(
            "test.txt",
            b"test file content",
            content_type="text/plain"
        )

    def test_home_page_loads(self):
        """Testa se a página inicial carrega corretamente"""
        response = self.client.get(self.upload_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'file_upload/home.html')

    def test_file_upload_success(self):
        """Testa o upload bem-sucedido de um arquivo"""
        data = {'description': 'Test file'}
        files = {'file': self.test_file}
        
        response = self.client.post(self.upload_url, data, files)
        
        self.assertEqual(response.status_code, 302)  # Redirect after success
        self.assertEqual(UploadedFile.objects.count(), 1)
        
        uploaded_file = UploadedFile.objects.first()
        self.assertEqual(uploaded_file.filename, "test.txt")
        self.assertEqual(uploaded_file.description, "Test file")

    def test_file_upload_without_file(self):
        """Testa o upload sem arquivo (deve falhar)"""
        data = {'description': 'Test file'}
        response = self.client.post(self.upload_url, data)
        
        self.assertEqual(response.status_code, 200)  # Stays on same page
        self.assertEqual(UploadedFile.objects.count(), 0)

    def test_file_list_view(self):
        """Testa a view de listagem de arquivos"""
        # Criar um arquivo de teste
        UploadedFile.objects.create(
            file=self.test_file,
            description="Test file"
        )
        
        response = self.client.get(reverse('file_upload:file_list'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'file_upload/file_list.html')
        self.assertEqual(len(response.context['files']), 1)

class FileUploadFormTest(TestCase):
    def test_valid_file_upload(self):
        """Testa o formulário com arquivo válido"""
        from .forms import FileUploadForm
        
        test_file = SimpleUploadedFile(
            "test.txt",
            b"test content",
            content_type="text/plain"
        )
        
        form_data = {'description': 'Test file'}
        file_data = {'file': test_file}
        
        form = FileUploadForm(form_data, file_data)
        self.assertTrue(form.is_valid())

    def test_file_size_limit(self):
        """Testa o limite de tamanho do arquivo"""
        from .forms import FileUploadForm
        
        # Criar um arquivo maior que 50MB
        large_content = b"x" * (51 * 1024 * 1024)  # 51MB
        large_file = SimpleUploadedFile(
            "large.txt",
            large_content,
            content_type="text/plain"
        )
        
        form_data = {'description': 'Large file'}
        file_data = {'file': large_file}
        
        form = FileUploadForm(form_data, file_data)
        self.assertFalse(form.is_valid())
        self.assertIn('O arquivo não pode ter mais de 50MB', str(form.errors))

    def test_invalid_file_extension(self):
        """Testa extensão de arquivo inválida"""
        from .forms import FileUploadForm
        
        invalid_file = SimpleUploadedFile(
            "test.exe",
            b"test content",
            content_type="application/x-msdownload"
        )
        
        form_data = {'description': 'Invalid file'}
        file_data = {'file': invalid_file}
        
        form = FileUploadForm(form_data, file_data)
        self.assertFalse(form.is_valid())
        self.assertIn('Extensão não permitida', str(form.errors))

class FileUploadAPITest(TestCase):
    def setUp(self):
        self.client = Client()
        self.api_url = reverse('file_upload:upload_api')
        self.test_file = SimpleUploadedFile(
            "test.txt",
            b"test file content",
            content_type="text/plain"
        )

    def test_api_upload_success(self):
        """Testa o upload via API"""
        data = {'description': 'Test file'}
        files = {'file': self.test_file}
        
        response = self.client.post(self.api_url, data, files)
        
        self.assertEqual(response.status_code, 200)
        response_data = response.json()
        self.assertTrue(response_data['success'])
        self.assertEqual(UploadedFile.objects.count(), 1)

    def test_api_upload_failure(self):
        """Testa falha no upload via API"""
        data = {'description': 'Test file'}
        # Sem arquivo
        
        response = self.client.post(self.api_url, data)
        
        self.assertEqual(response.status_code, 200)
        response_data = response.json()
        self.assertFalse(response_data['success'])
        self.assertEqual(UploadedFile.objects.count(), 0)
