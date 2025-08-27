from django.db import models
from django.utils import timezone
import os

def upload_to(instance, filename):
    """Função para definir o caminho de upload dos arquivos"""
    # Cria um diretório baseado na data atual
    date_path = timezone.now().strftime('%Y/%m/%d')
    return os.path.join('uploads', date_path, filename)

class UploadedFile(models.Model):
    """Modelo para armazenar informações sobre arquivos enviados"""
    file = models.FileField(upload_to=upload_to)
    filename = models.CharField(max_length=255)
    file_size = models.BigIntegerField()
    file_type = models.CharField(max_length=100)
    uploaded_at = models.DateTimeField(auto_now_add=True)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.filename

    def save(self, *args, **kwargs):
        if not self.filename:
            self.filename = os.path.basename(self.file.name)
        if not self.file_size:
            self.file_size = self.file.size
        if not self.file_type:
            self.file_type = os.path.splitext(self.file.name)[1]
        super().save(*args, **kwargs)

    class Meta:
        ordering = ['-uploaded_at']
        verbose_name = 'Arquivo Enviado'
        verbose_name_plural = 'Arquivos Enviados'
