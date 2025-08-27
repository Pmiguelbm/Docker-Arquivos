from django import forms
from .models import UploadedFile

class FileUploadForm(forms.ModelForm):
    """Formulário para upload de arquivos"""
    
    class Meta:
        model = UploadedFile
        fields = ['file', 'description']
        widgets = {
            'file': forms.FileInput(attrs={
                'class': 'form-control',
                'accept': '*/*',
                'id': 'file-input'
            }),
            'description': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 3,
                'placeholder': 'Descrição do arquivo (opcional)'
            })
        }
    
    def clean_file(self):
        file = self.cleaned_data.get('file')
        if file:
            # Verificar tamanho do arquivo (máximo 50MB)
            if file.size > 50 * 1024 * 1024:
                raise forms.ValidationError('O arquivo não pode ter mais de 50MB.')
            
            # Verificar extensões permitidas (opcional)
            allowed_extensions = ['.txt', '.pdf', '.doc', '.docx', '.jpg', '.jpeg', '.png', '.gif', '.zip', '.rar']
            file_extension = '.' + file.name.split('.')[-1].lower()
            if file_extension not in allowed_extensions:
                raise forms.ValidationError(f'Extensão não permitida. Extensões permitidas: {", ".join(allowed_extensions)}')
        
        return file
