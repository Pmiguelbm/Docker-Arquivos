from django.contrib import admin
from .models import UploadedFile

@admin.register(UploadedFile)
class UploadedFileAdmin(admin.ModelAdmin):
    list_display = ['filename', 'file_type', 'file_size', 'uploaded_at']
    list_filter = ['file_type', 'uploaded_at']
    search_fields = ['filename', 'description']
    readonly_fields = ['file_size', 'uploaded_at']
    
    def get_queryset(self, request):
        return super().get_queryset(request).order_by('-uploaded_at')
