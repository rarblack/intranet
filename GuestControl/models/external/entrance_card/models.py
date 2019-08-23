from django.db import models
from django.conf import settings
from django.utils import timezone

from . import choices


def upload_image_to(instance, filename):
    return 'guest_control/external/visitor/entrance_card/images/{0}'.format(filename)


class ExternalEntranceCardModel(models.Model):

    image = models.FileField(upload_to=upload_image_to)

    name = models.CharField(max_length=150)

    surname = models.CharField(max_length=150)

    company = models.CharField(max_length=150)

    status = models.IntegerField(
        choices=choices.STATUSES,
        default=0
    )

    enter_datetime = models.DateTimeField(
        null=True,
        blank=True,
        default=None,
        verbose_name='Actual Enter Time',
        help_text='Please fill in yyyy-mm-dd hh:mm:ss format'
    )

    leave_datetime = models.DateTimeField(
        null=True,
        blank=True,
        default=None,
        verbose_name='Actual Leave Time',
        help_text = 'Please fill in yyyy-mm-dd hh:mm:ss format'
    )

    processor = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        default=None,
        related_name='guestControl_visitor_entranceCard_cardModel_processor'
    )

    procession_datetime = models.DateTimeField(
        null=True,
        blank=True,
        default=None
    )

    creator = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        null=True,
        on_delete=models.SET_NULL,
        verbose_name='Creator',
        related_name='guestControl_visitor_entrance_card_cardModel_creator'
    )

    creation_datetime = models.DateTimeField(
        default=timezone.now,
        verbose_name='Creation time'
    )

    class Meta:
        verbose_name = 'External Entrance Cards'
        verbose_name_plural = 'External Entrance Cards'

    def get_full_name(self):
        return '{0} {1}'.format(self.name, self.surname)
