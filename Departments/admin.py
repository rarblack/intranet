from django.contrib import admin

from . import models

# Register your models here.


@admin.register(models.WellDataStatModel)
class WellDataStatModelAdmin(admin.ModelAdmin):
    display_list = ['id', 'subject' ]


