from django.contrib.auth.models import User
from django.conf import settings
from django.db import models
from django.utils import timezone

from .choices import STATUSES, SUBJECTS, PRIORITY_SCALES, REASONS, CATEGORIES
from CommonItems.models import WorkArea


class Material(models.Model):
    name = models.CharField(max_length=100)

    category = models.IntegerField(choices=CATEGORIES,
                                   default=0)

    created_by = models.ForeignKey(settings.AUTH_USER_MODEL,
                                   on_delete=models.SET_NULL,
                                   null=True,
                                   related_name='warehouse_material_created_by')

    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.name


class Ticket(models.Model):

    subject = models.CharField(max_length=150)

    material = models.ManyToManyField(Material)

    location = models.ForeignKey(WorkArea,
                                 null=True,
                                 on_delete=models.SET_NULL,
                                 related_name='warehouse_ticket_location')

    importance = models.IntegerField(choices=PRIORITY_SCALES,
                                     default=0)

    note = models.TextField(max_length=500,
                            verbose_name="Additional note")

    detail = models.OneToOneField('TicketDetail',
                                  on_delete=models.CASCADE)

    def __str__(self):
        return str(self.id)


class TicketDetail(models.Model):

    status = models.IntegerField(choices=STATUSES,
                                 default=0)

    assignee = models.ForeignKey(settings.AUTH_USER_MODEL,
                                 on_delete=models.SET_NULL,
                                 null=True,
                                 blank=True,
                                 default=None,
                                 related_name='warehouse_ticket_assignee')

    processed_by = models.ForeignKey(settings.AUTH_USER_MODEL,
                                     on_delete=models.SET_NULL,
                                     null=True,
                                     blank=True,
                                     default=None,
                                     related_name='warehouse_ticket_processed_by')

    processed_at = models.DateTimeField(null=True,
                                        blank=True,
                                        default=None)

    created_by = models.ForeignKey(settings.AUTH_USER_MODEL,
                                   on_delete=models.SET_NULL,
                                   null=True,
                                   related_name='warehouse_ticket_created_by')

    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return 'ID: {0}'.format(self.pk)

    class Meta:
        verbose_name = 'Ticket'
        verbose_name_plural = 'Tickets'


class Message(models.Model):

    ticket = models.OneToOneField(Ticket,
                                  on_delete=models.SET_NULL,
                                  null=True)
    message = models.CharField(max_length=500)

    created_by = models.ForeignKey(settings.AUTH_USER_MODEL,
                                   on_delete=models.SET_NULL,
                                   null=True,
                                   related_name='warehouse_message_created_by')

    created_at = models.DateTimeField(default=timezone.now)

    class Meta:
        verbose_name_plural = "Messages"

    def __str__(self):
        return 'ID: {0}'.format(self.id)


class Activity(models.Model):
    detail = models.ForeignKey(TicketDetail,
                               on_delete=models.CASCADE)

    status = models.IntegerField(choices=STATUSES)

    assignee = models.ForeignKey(settings.AUTH_USER_MODEL,
                                 on_delete=models.SET_NULL,
                                 null=True,
                                 blank=True,
                                 related_name='warehouse_activity_assignee')

    created_by = models.ForeignKey(settings.AUTH_USER_MODEL,
                                   on_delete=models.SET_NULL,
                                   null=True,
                                   related_name='warehouse_activity_created_by')

    created_at = models.DateTimeField(default=timezone.now)

    class Meta:
        verbose_name_plural = 'Activities'

    def __str__(self):
        return 'ID: {0} Ticket ID: {1}'.format(self.id, self.detail_id)



