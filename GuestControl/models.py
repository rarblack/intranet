from django.db import models
from django.conf import settings
from django.utils import timezone

from CommonItems.models import WorkArea
from .choices import STATUSES, PRIORITY_SCALES, CONTACT_TYPES, PURPOSES_EXTERNAL, PURPOSES_INTERNAL


class ExternalVisitTicket(models.Model):

    name = models.CharField(max_length=150)

    surname = models.CharField(max_length=150)

    company = models.CharField(max_length=150)

    subject = models.CharField(max_length=254)

    purpose = models.IntegerField(choices=PURPOSES_EXTERNAL,
                                  default=0)

    contact_type = models.IntegerField(choices=CONTACT_TYPES,
                                       default=0)

    contact = models.CharField(max_length=150)

    email = models.EmailField(max_length=254)

    host = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.SET_NULL,
                             null=True,
                             related_name='guestcontrol_external_visit_ticket_host')

    visit_datetime = models.DateTimeField(default=timezone.now)

    leave_datetime = models.DateTimeField()

    importance = models.IntegerField(choices=PRIORITY_SCALES,
                                     default=0)

    note = models.TextField(max_length=500,
                            verbose_name="Additional note",
                            blank=True,
                            null=True)

    detail = models.OneToOneField('ExternalVisitTicketDetail',
                                  on_delete=models.CASCADE)


class ExternalVisitTicketDetail(models.Model):

    status = models.IntegerField(choices=STATUSES,
                                 default=0)

    visited_at = models.DateTimeField(null=True,
                                      blank=True,
                                      default=None,
                                      verbose_name='Actual Enter Time')

    left_at = models.DateTimeField(null=True,
                                   blank=True,
                                   default=None,
                                   verbose_name='Actual Leave Time')

    processed_by = models.ForeignKey(settings.AUTH_USER_MODEL,
                                     on_delete=models.SET_NULL,
                                     null=True,
                                     blank=True,
                                     default=None,
                                     related_name='guestcontrol_external_visit_ticket_detail_processed_by')

    processed_at = models.DateTimeField(null=True,
                                        blank=True,
                                        default=None)

    created_by = models.ForeignKey(settings.AUTH_USER_MODEL,
                                   null=True,
                                   on_delete=models.SET_NULL,
                                   verbose_name='Creator',
                                   related_name='guestcontrol_external_visit_ticket_created_by')

    created_at = models.DateTimeField(default=timezone.now,
                                      verbose_name='Creation time')

    class Meta:
        verbose_name_plural = 'External Visit Tickets'


class InternalVisitTicket(models.Model):

    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.SET_NULL,
                             null=True,
                             related_name='guestcontrol_internal_visit_ticket_user')

    subject = models.CharField(max_length=254)

    purpose = models.IntegerField(choices=PURPOSES_INTERNAL,
                                  default=0)

    host = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.SET_NULL,
                             null=True,
                             related_name='guestcontrol_internal_visit_ticket_host')

    visit_datetime = models.DateTimeField(default=timezone.now)

    leave_datetime = models.DateTimeField(help_text='Please fill in yyyy-mm-dd hh:mm:ss format')

    importance = models.IntegerField(choices=PRIORITY_SCALES,
                                     default=0)

    note = models.TextField(max_length=500,
                            verbose_name="Additional note",
                            blank=True,
                            null=True,)

    detail = models.OneToOneField('InternalVisitTicketDetail',
                                  on_delete=models.CASCADE)


class InternalVisitTicketDetail(models.Model):

    status = models.IntegerField(choices=STATUSES,
                                 default=0)

    visited_at = models.DateTimeField(null=True,
                                      blank=True,
                                      default=None,
                                      verbose_name='Actual Enter Time')

    left_at = models.DateTimeField(null=True,
                                   blank=True,
                                   default=None,
                                   verbose_name='Actual Leave Time')

    processed_by = models.ForeignKey(settings.AUTH_USER_MODEL,
                                     on_delete=models.SET_NULL,
                                     null=True,
                                     blank=True,
                                     default=None,
                                     related_name='guestcontrol_internal_visit_ticket_detail_processed_by')

    processed_at = models.DateTimeField(null=True,
                                        blank=True,
                                        default=None)

    created_by = models.ForeignKey(settings.AUTH_USER_MODEL,
                                   null=True,
                                   on_delete=models.SET_NULL,
                                   verbose_name='Creator',
                                   related_name='guestcontrol_internal_visit_ticket_created_by')

    created_at = models.DateTimeField(default=timezone.now,
                                      verbose_name='Creation time')

    class Meta:
        verbose_name_plural = 'Internal Visit Tickets'

    def __str__(self):
        return 'ID: {0}'.format(self.pk)


class DetailAbstractModel(models.Model):

    status = models.IntegerField(choices=STATUSES,
                                 default=0)

    enter_datetime = models.DateTimeField(null=True,
                                          blank=True,
                                          default=None,
                                          verbose_name='Actual Enter Time')

    leave_datetime = models.DateTimeField(null=True,
                                          blank=True,
                                          default=None,
                                          verbose_name='Actual Leave Time')

    procession_datetime = models.DateTimeField(null=True,
                                               blank=True,
                                               default=None)

    creation_datetime = models.DateTimeField(default=timezone.now,
                                             verbose_name='Creation time')

    class Meta:
        abstract = True


def upload_image_to(instance, filename):
    return f'guest_control/visitor_entrance_card_images/{filename}'


class VisitorEntranceCardModel(DetailAbstractModel):

    image = models.FileField(upload_to=upload_image_to)

    name = models.CharField(max_length=150)

    surname = models.CharField(max_length=150)

    company = models.CharField(max_length=150)

    processor = models.ForeignKey(settings.AUTH_USER_MODEL,
                                  on_delete=models.SET_NULL,
                                  null=True,
                                  blank=True,
                                  default=None,
                                  related_name='guestcontrol_visitor_entrance_card_processor')

    creator = models.ForeignKey(settings.AUTH_USER_MODEL,
                                null=True,
                                on_delete=models.SET_NULL,
                                verbose_name='Creator',
                                related_name='guestcontrol_visitor_entrance_card_creator')