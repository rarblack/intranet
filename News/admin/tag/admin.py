from django.contrib import admin
from django.utils import timezone

from ...models.tag import models


@admin.register(models.TagModel)
class TagAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'created_by', 'created_at')