from django.conf import settings
from django.db import models
from django.utils import timezone

from .choices import BRAND_TYPE, MODEL_TYPE, CAR_TYPE, TRIP_TYPE, STATUSES, PRIORITY_SCALES, REASONS


class Car(models.Model):
    brand = models.IntegerField(choices=BRAND_TYPE,
                                default=0)
    model = models.IntegerField(choices=MODEL_TYPE,
                                default=0)
    type = models.IntegerField(choices=CAR_TYPE,
                               default=0)
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL,
                                   on_delete=models.SET_NULL,
                                   null=True,
                                   related_name='transportation_car_created_by')
    created_at = models.DateTimeField(default=timezone.now)

    class Meta:
        verbose_name_plural = 'Cars'

    def __str__(self):
        return '{0}-{1} ({2})'.format(self.brand,
                                      self.model,
                                      self.get_type_display())


class Ticket(models.Model):
    car = models.ForeignKey(Car,
                            on_delete=models.SET_NULL,
                            null=True,
                            related_name='transportation_ticket_car')

    trip = models.IntegerField(choices=TRIP_TYPE,
                               default=1)

    origin = models.CharField(max_length=100)

    destination = models.CharField(max_length=500)

    leave_time = models.DateTimeField()

    return_time = models.DateTimeField()

    duration = models.CharField(max_length=50,
                                null=True)

    importance = models.IntegerField(choices=PRIORITY_SCALES,
                                     default=0)

    note = models.TextField(max_length=500,
                            verbose_name="Additional note")

    detail = models.OneToOneField('TicketDetail',
                                  on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = "Tickets"

    def __str__(self):
        return 'ID: {0} Type: {1}'.format(self.id, TRIP_TYPE[self.trip][1])

    # def get_absolute_path(self):
    #     return reverse('one', args=[str(self.id)])


class TicketDetail(models.Model):
    status = models.IntegerField(choices=STATUSES)

    assignee = models.ForeignKey(settings.AUTH_USER_MODEL,
                                 on_delete=models.SET_NULL,
                                 null=True,
                                 blank=True,
                                 default=None,
                                 related_name='transportation_ticket_detail_assignee', )

    processed_by = models.ForeignKey(settings.AUTH_USER_MODEL,
                                     on_delete=models.SET_NULL,
                                     null=True,
                                     blank=True,
                                     default=None,
                                     related_name='transportation_ticket_detail_processed_by')

    processed_at = models.DateTimeField(null=True,
                                        blank=True,
                                        default=None)

    created_by = models.ForeignKey(settings.AUTH_USER_MODEL,
                                   on_delete=models.SET_NULL,
                                   null=True,
                                   related_name='transportation_ticket_detail_created_by')

    created_at = models.DateTimeField(default=timezone.now)

    class Meta:
        verbose_name_plural = 'Ticket Details'

    def __str__(self):
        return 'ID: {0}'.format(self.pk)


class Message(models.Model):

    ticket = models.ForeignKey(Ticket,
                               on_delete=models.CASCADE)

    reason = models.IntegerField(choices=REASONS,
                                 default=0)

    message = models.TextField(max_length=500,
                               default='This is a entrance_card when tickets is created.')

    created_by = models.ForeignKey(settings.AUTH_USER_MODEL,
                                   on_delete=models.SET_NULL,
                                   null=True,
                                   related_name='transportation_message_created_by')

    created_at = models.DateTimeField(default=timezone.now)

    class Meta:
        verbose_name_plural = "Messages"

    def __str__(self):
        return 'ID: {0} Reason: {1}'.format(self.id, REASONS[self.reason][1])


class Activity(models.Model):

    detail = models.ForeignKey(TicketDetail,
                               on_delete=models.CASCADE)

    status = models.IntegerField(choices=STATUSES)

    assignee = models.ForeignKey(settings.AUTH_USER_MODEL,
                                 on_delete=models.SET_NULL,
                                 null=True,
                                 blank=True,
                                 related_name='transportation_activity_assignee')

    created_by = models.ForeignKey(settings.AUTH_USER_MODEL,
                                   on_delete=models.SET_NULL,
                                   null=True,
                                   related_name='transportation_activity_created_by')

    created_at = models.DateTimeField(default=timezone.now)

    class Meta:
        verbose_name_plural = 'Activities'

    def __str__(self):
        return 'ID: {0} Ticket ID: {1}'.format(self.id, self.detail_id)
