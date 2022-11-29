from django.contrib import admin
from .models import *
# Register your models here.
@admin.register(Folder)
class FolderAdmin(admin.ModelAdmin):
    list_display = ['id' ,'folder_name', 'folder']

@admin.register(File)
class FileAdmin(admin.ModelAdmin):
    list_display = ['id' ,'folder', 'file']
