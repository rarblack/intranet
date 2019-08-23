from django.db import models
from django.conf import settings
from django.utils import timezone

from .choices import STATUSES, PRIORITY_SCALES, PURPOSES


class InternalVisitorTicketModel(models.Model):

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        related_name='guestControl_internal_visitor_internalVisitorTicketModel_user'
    )

    subject = models.CharField(max_length=254)

    purpose = models.IntegerField(
        choices=PURPOSES,
        default=0
    )

    host = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        related_name='guestControl_internal_visitor_ticketModel_host'
    )

    visit_datetime = models.DateTimeField(
        help_text='Please fill in yyyy-mm-dd hh:mm:ss format'
    )

    leave_datetime = models.DateTimeField(
        help_text='Please fill in yyyy-mm-dd hh:mm:ss format'
    )

    importance = models.IntegerField(
        choices=PRIORITY_SCALES,
        default=0
    )

    note = models.TextField(
        max_length=500,
        verbose_name="Additional note",
        blank=True,
        null=True
    )

    detail = models.OneToOneField(
        'InternalVisitorTicketDetailModel',
        on_delete=models.CASCADE
    )


class InternalVisitorTicketDetailModel(models.Model):

    status = models.IntegerField(
        choices=STATUSES,
        default=0
    )

    visited_at = models.DateTimeField(
        null=True,
        blank=True,
        default=None,
        verbose_name='Actual Enter Time'
    )

    left_at = models.DateTimeField(
        null=True,
        blank=True,
        default=None,
        verbose_name='Actual Leave Time'
    )

    processed_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        default=None,
        related_name='guestControl_internal_visitor_internalVisitorTicketDetailModel_processed_by'
    )

    processed_at = models.DateTimeField(
        null=True,
        blank=True,
        default=None
    )

    created_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        null=True,
        on_delete=models.SET_NULL,
        verbose_name='Creator',
        related_name='guestControl_internal_visitor_ticketDetailModel_created_by'
    )

    created_at = models.DateTimeField(
        default=timezone.now,
        verbose_name='Creation time'
    )

    class Meta:
        verbose_name = 'Internal Visitor Ticket'
        verbose_name_plural = 'Internal Visitor Tickets'

    def __str__(self):
        return 'ID: {0}'.format(self.pk)

