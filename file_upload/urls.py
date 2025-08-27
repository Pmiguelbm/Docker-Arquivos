from django.urls import path
from . import views

app_name = 'file_upload'

urlpatterns = [
    path('', views.home, name='home'),
    path('files/', views.file_list, name='file_list'),
    path('upload/', views.upload_file_api, name='upload_api'),
    path('delete/<int:file_id>/', views.delete_file, name='delete_file'),
]
