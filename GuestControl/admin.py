from django.contrib import admin
from django.utils import timezone

from .models import ExternalVisitTicket, ExternalVisitTicketDetail, InternalVisitTicket, InternalVisitTicketDetail


#                                                                                              ExternalVisitTicketInline
class ExternalVisitTicketInline(admin.StackedInline):
    model = ExternalVisitTicket
    can_delete = False
    verbose_name_plural = 'External Visit Ticket'
    fk_name = 'detail'

#                                                                                         ExternalVisitTicketDetailAdmin
@admin.register(ExternalVisitTicketDetail)
class ExternalVisitTicketDetailAdmin(admin.ModelAdmin):
    inlines = (ExternalVisitTicketInline, )
    list_display = ('id', 'status', 'created_by', 'created_at')

    def save_model(self, request, obj, form, change):
        if not change:
            obj.created_by = request.user
            obj.created_at = timezone.now()
            super().save_model(request, obj, form, change)
        elif change:
            super().save_model(request, obj, form, change)


#                                                                                              InternalVisitTicketInline
class InternalVisitTicketInline(admin.StackedInline):
    model = InternalVisitTicket
    can_delete = False
    verbose_name_plural = 'Internal Visit Ticket'
    fk_name = 'detail'


#                                                                                         InternalVisitTicketDetailAdmin
@admin.register(InternalVisitTicketDetail)
class InternalVisitTicketDetailAdmin(admin.ModelAdmin):
    inlines = (InternalVisitTicketInline, )
    list_display = ('id', 'status', 'created_by', 'created_at')

    def save_model(self, request, obj, form, change):
        if not change:
            obj.created_by = request.user
            obj.created_at = timezone.now()
            super().save_model(request, obj, form, change)
        elif change:
            super().save_model(request, obj, form, change)



