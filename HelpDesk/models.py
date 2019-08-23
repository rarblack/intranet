from django.conf import settings
from django.db import models
from django.urls import reverse
from django.utils import timezone

from .choices import TICKET_TYPES, STATUSES, REASONS, PRIORITY_SCALES
from CommonItems.models import WorkArea


def user_directory_path(instance, filename):
    return '{0}/{1}/{2}/{3}'.format('helpdesk',
                                    instance.detail.created_by.username,
                                    TICKET_TYPES[instance.type][1],
                                    filename)


class Ticket(models.Model):

    type = models.IntegerField(choices=TICKET_TYPES,
                               default=0)

    subject = models.CharField(max_length=150)

    location = models.ForeignKey(WorkArea,
                                 null=True,
                                 on_delete=models.SET_NULL)

    file = models.FileField(upload_to=user_directory_path,
                            null=True,
                            blank=True,
                            default=None)

    importance = models.IntegerField(choices=PRIORITY_SCALES,
                                     default=0)

    note = models.TextField(max_length=500,
                            default='Description has not been provided.')

    detail = models.OneToOneField('TicketDetail',
                                  on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = "Tickets"

    def __str__(self):
        return 'ID: {0} Type: {1}'.format(self.id, TICKET_TYPES[self.type][1])


class TicketDetail(models.Model):

    status = models.IntegerField(choices=STATUSES)

    assignee = models.ForeignKey(settings.AUTH_USER_MODEL,
                                 on_delete=models.SET_NULL,
                                 null=True,
                                 blank=True,
                                 default=None,
                                 related_name='helpdesk_ticket_assignee',)

    processed_by = models.ForeignKey(settings.AUTH_USER_MODEL,
                                     on_delete=models.SET_NULL,
                                     null=True,
                                     blank=True,
                                     default=None,
                                     related_name='helpdesk_ticket_processed_by')

    processed_at = models.DateTimeField(null=True,
                                        blank=True,
                                        default=None)

    created_by = models.ForeignKey(settings.AUTH_USER_MODEL,
                                   on_delete=models.SET_NULL,
                                   null=True,
                                   related_name='helpdesk_ticket_detail_created_by')

    created_at = models.DateTimeField(default=timezone.now)

    class Meta:
        verbose_name_plural = 'Tickets'

    def __str__(self):
        return 'ID: {0}'.format(self.pk)


class Activity(models.Model):

    detail = models.ForeignKey(TicketDetail,
                               on_delete=models.CASCADE)

    status = models.IntegerField(choices=STATUSES)

    assignee = models.ForeignKey(settings.AUTH_USER_MODEL,
                                 on_delete=models.SET_NULL,
                                 null=True,
                                 blank=True,
                                 related_name='helpdesk_activity_assignee')

    created_by = models.ForeignKey(settings.AUTH_USER_MODEL,
                                   on_delete=models.SET_NULL,
                                   null=True,
                                   related_name='helpdesk_activity_created_by')

    created_at = models.DateTimeField(editable=False)

    class Meta:
        verbose_name_plural = 'Activities'

    def __str__(self):
        return 'ID: {0} Ticket ID: {1}'.format(self.id, self.detail_id)


class Message(models.Model):

    ticket = models.ForeignKey(Ticket,
                               on_delete=models.CASCADE)

    reason = models.IntegerField(choices=REASONS,
                                 default=0)

    explanation = models.TextField(max_length=500,
                                   default='This is a entrance_card when tickets is created.')

    created_by = models.ForeignKey(settings.AUTH_USER_MODEL,
                                   on_delete=models.SET_NULL,
                                   null=True,
                                   related_name='helpdesk_message_created_by')

    created_at = models.DateTimeField(default=timezone.now)

    class Meta:
        verbose_name_plural = "Messages"

    def __str__(self):
        return 'ID: {0} Reason: {1}'.format(self.id, REASONS[self.reason][1])
