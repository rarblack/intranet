from django.contrib import admin
from django.utils import timezone

from ...models.post import models


@admin.register(models.PostModel)
class TicketDetailAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'category', 'created_by', 'created_at')

    def save_model(self, request, obj, form, change):
        if not change:
            obj.created_by = request.user
            obj.created_at = timezone.now()
            super().save_model(request, obj, form, change)
        elif change:
            super().save_model(request, obj, form, change)