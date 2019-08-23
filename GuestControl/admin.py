from django.contrib import admin
from django.utils import timezone

from GuestControl.models.internal.visitor import models as internal_visitor_models
from GuestControl.models.external.visitor import models as external_visitor_models
from GuestControl.models.external.entrance_card import models as external_entrance_models


class ExternalVisitorTicketInline(admin.StackedInline):
    model = external_visitor_models.ExternalVisitorTicketModel
    can_delete = False
    verbose_name_plural = 'External Visit Ticket'
    fk_name = 'detail'


@admin.register(external_visitor_models.ExternalVisitorTicketDetailModel)
class TicketDetailAdmin(admin.ModelAdmin):
    inlines = (ExternalVisitorTicketInline, )
    list_display = ('id', 'status', 'created_by', 'created_at')

    def save_model(self, request, obj, form, change):
        if not change:
            obj.created_by = request.user
            obj.created_at = timezone.now()
            super().save_model(request, obj, form, change)
        elif change:
            super().save_model(request, obj, form, change)


class InternalVisitorTicketInline(admin.StackedInline):
    model = internal_visitor_models.InternalVisitorTicketModel
    can_delete = False
    verbose_name_plural = 'Internal Visit Ticket'
    fk_name = 'detail'


@admin.register(internal_visitor_models.InternalVisitorTicketDetailModel)
class InternalVisitorTicketDetailAdmin(admin.ModelAdmin):
    inlines = (InternalVisitorTicketInline, )
    list_display = ('id', 'status', 'created_by', 'created_at')

    def save_model(self, request, obj, form, change):
        if not change:
            obj.created_by = request.user
            obj.created_at = timezone.now()
            super().save_model(request, obj, form, change)
        elif change:
            super().save_model(request, obj, form, change)


@admin.register(external_entrance_models.ExternalEntranceCardModel)
class ExternalEntranceCardAdmin(admin.ModelAdmin):
    display_list = ('id', 'name', 'surname', 'company')


