from django.contrib import admin
from . import models


@admin.register(models.UploadFiles)
class UploadFiles(admin.ModelAdmin):
    display_list = ['id','short_description']
