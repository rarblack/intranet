from django.contrib import admin
from . import models


@admin.register(models.DocumentModel)
class UploadFiles(admin.ModelAdmin):
    display_list = ['id', 'file_name']
