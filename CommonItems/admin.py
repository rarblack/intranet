from django.contrib import admin

from .models import WorkArea


@admin.register(WorkArea)
class WorkAreaAdmin(admin.ModelAdmin):
    display_list = ['id','short_description']
