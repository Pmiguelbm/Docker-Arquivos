from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods
from .models import UploadedFile
from .forms import FileUploadForm
import json

def home(request):
    """View principal que mostra o formulário de upload e lista de arquivos"""
    if request.method == 'POST':
        form = FileUploadForm(request.POST, request.FILES)
        if form.is_valid():
            uploaded_file = form.save()
            messages.success(request, f'Arquivo "{uploaded_file.filename}" enviado com sucesso!')
            return redirect('home')
        else:
            messages.error(request, 'Erro ao enviar arquivo. Verifique os dados.')
    else:
        form = FileUploadForm()
    
    files = UploadedFile.objects.all()
    return render(request, 'file_upload/home.html', {
        'form': form,
        'files': files
    })

@csrf_exempt
@require_http_methods(["POST"])
def upload_file_api(request):
    """API para upload de arquivos via AJAX"""
    try:
        form = FileUploadForm(request.POST, request.FILES)
        if form.is_valid():
            uploaded_file = form.save()
            return JsonResponse({
                'success': True,
                'message': f'Arquivo "{uploaded_file.filename}" enviado com sucesso!',
                'file': {
                    'id': uploaded_file.id,
                    'filename': uploaded_file.filename,
                    'file_size': uploaded_file.file_size,
                    'file_type': uploaded_file.file_type,
                    'uploaded_at': uploaded_file.uploaded_at.isoformat(),
                    'url': uploaded_file.file.url
                }
            })
        else:
            return JsonResponse({
                'success': False,
                'message': 'Erro ao enviar arquivo.',
                'errors': form.errors
            })
    except Exception as e:
        return JsonResponse({
            'success': False,
            'message': f'Erro interno: {str(e)}'
        })

def file_list(request):
    """View para listar todos os arquivos enviados"""
    files = UploadedFile.objects.all()
    return render(request, 'file_upload/file_list.html', {
        'files': files
    })

def delete_file(request, file_id):
    """View para deletar um arquivo"""
    try:
        file_obj = UploadedFile.objects.get(id=file_id)
        filename = file_obj.filename
        file_obj.delete()
        messages.success(request, f'Arquivo "{filename}" deletado com sucesso!')
    except UploadedFile.DoesNotExist:
        messages.error(request, 'Arquivo não encontrado.')
    
    return redirect('home')
