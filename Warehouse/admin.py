from django.contrib import admin
from .models import Ticket, TicketDetail, Activity, Message, Material
from django.utils import timezone


@admin.register(Material)
class MaterialAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')

    def save_model(self, request, obj, form, change):
        if not change:
            obj.created_by = request.user
            obj.created_at = timezone.now()
            super().save_model(request, obj, form, change)


class TicketInline(admin.StackedInline):
    model = Ticket
    can_delete = False
    verbose_name_plural = 'Ticket'
    fk_name = 'detail'


@admin.register(TicketDetail)
class TicketDetailAdmin(admin.ModelAdmin):
    inlines = (TicketInline, )
    list_display = ('id', 'assignee', 'processed_by', 'processed_at', 'created_by', 'created_at')

    # def get_file_name(self, instance):
    #     file_name = re.findall(r'(?<=/).*?(?=\.)', instance.file.name)
    #     return file_name
    # get_file_name.short_description = 'file_name'

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

    list_display = ('id', 'message')

    def save_model(self, request, obj, form, change):
        if not change:
            obj.created_by = request.user
            obj.created_at = timezone.now()
            super().save_model(request, obj, form, change)