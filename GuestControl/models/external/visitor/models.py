from django.db import models
from django.conf import settings
from django.utils import timezone

from .choices import STATUSES, PRIORITY_SCALES, CONTACT_TYPES, PURPOSES


class ExternalVisitorTicketModel(models.Model):

    name = models.CharField(max_length=150)

    surname = models.CharField(max_length=150)

    company = models.CharField(max_length=150)

    subject = models.CharField(max_length=254)

    purpose = models.IntegerField(
        choices=PURPOSES,
        default=0
    )

    contact_type = models.IntegerField(
        choices=CONTACT_TYPES,
        default=0
    )

    contact = models.CharField(max_length=150)

    email = models.EmailField(max_length=254)

    host = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        related_name='guestControl_external_visitor_externalVisitorTicketModel_host'
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
        'ExternalVisitorTicketDetailModel',
        on_delete=models.CASCADE
    )


class ExternalVisitorTicketDetailModel(models.Model):

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
        related_name='guestControl_external_visitor_externalVisitorTicketDetailModel_processed_by'
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
        related_name='guestControl_external_visitor_externalVisitorTicketDetailModel_created_by'
    )

    created_at = models.DateTimeField(
        default=timezone.now,
        verbose_name='Creation time'
    )

    class Meta:
        verbose_name = 'External Visitor Ticket'
        verbose_name_plural = 'External Visitor Tickets'
