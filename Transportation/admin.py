from django.contrib import admin
from django.utils import timezone

from .models import Car, Ticket, TicketDetail, Activity, Message


@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    list_display = ('brand', 'model', 'type')


class TicketInline(admin.StackedInline):
    model = Ticket
    can_delete = False
    verbose_name_plural = 'Ticket'
    fk_name = 'detail'


@admin.register(TicketDetail)
class TicketDetailAdmin(admin.ModelAdmin):
    inlines = (TicketInline, )
    list_display = ('id', 'status', 'created_by', 'created_at')

    def save_model(self, request, obj, form, change):
        if not change:
            obj.created_by = request.user
            obj.created_at = timezone.now()
            super().save_model(request, obj, form, change)
        elif change:
            super().save_model(request, obj, form, change)


@admin.register(Activity)
class ActivityAdmin(admin.ModelAdmin):
    list_display = ('id', 'get_ticket_id', 'status', 'created_by', 'created_at')

    def get_ticket_id(self, instance):
        return instance.detail_id
    get_ticket_id.short_description = 'ticket_id'


@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):

    list_display = ('id', 'reason')

    def save_model(self, request, obj, form, change):
        if not change:
            obj.created_by = request.user
            obj.created_at = timezone.now()
            super().save_model(request, obj, form, change)


