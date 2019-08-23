from django.db import models
from HumanResources.models import Profile
from django.conf import settings
# from django.db.models.signals import post_save
# from django.dispatch import receiver
# from django.utils import timezone
import uuid
from django.contrib.auth.models import User


class EmployeeInstance(models.Model):
    class Meta:
        permissions = (
                        ("can_update_end_date", "Update the end date"),
                        ("can_add_instance", "Add a new employee instance")
                       )
    SQUAD_ORDER = (
        ('1', 'First squad'),
        ('2', 'Second squad')
    )
    id = models.UUIDField(primary_key=True,
                          default=uuid.uuid4, help_text='Unique ID for this particular employee across whole P.O.B.')
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, related_name='user_pobapp_related', editable=False, blank=True, null=True, verbose_name="Assigner's name")
    employee = models.ForeignKey('Employee', on_delete=models.SET_NULL, blank=True, null=True, verbose_name="Employee's name")
    work_place = models.ForeignKey('WorkPlace', on_delete=models.SET_NULL, blank=True, null=True, verbose_name="Assigned work place")
    start_time = models.DateTimeField(editable=False, auto_now_add=True)
    end_time = models.DateTimeField()
    note = models.CharField(max_length=30, verbose_name="Note", default='SOCAR-AQS')
    squad_order = models.CharField(max_length=5, choices=SQUAD_ORDER, editable=True)
    is_terminated = models.BooleanField(verbose_name='is terminated', default=False)

    def __str__(self):
        return 'Assigner: {0} | Employee: {1} | Work place: {2}'.format(self.user, self.employee, self.work_place)


class Employee(models.Model):
    STATUS = (
        ('a', 'Available'),
        ('r', 'Reserved'),
        ('s', 'Sick'),
        ('v', 'Vacation'),
        ('o', 'Others')
    )
    first_name = models.CharField(max_length=15)
    last_name = models.CharField(max_length=15)
    middle_name = models.CharField(max_length=15)
    work_id_card_name = models.CharField(max_length=15)
    id_card_name = models.CharField(max_length=15)
    profession_object = models.ForeignKey('Profession', on_delete=models.SET_NULL, blank=True, null=True, verbose_name="Profession")
    transportation_object = models.ForeignKey('Transportation', on_delete=models.SET_NULL, blank=True, null=True, verbose_name="Transport")
    company_object = models.ForeignKey('Company', on_delete=models.SET_NULL, blank=True, null=True, verbose_name="Company")
    status = models.CharField(max_length=1, choices=STATUS, default='a')

    def __str__(self):
        return '{0} {1} {2}'.format(self.first_name, self.last_name, self.middle_name,)


class Profession(models.Model):
    profession_name = models.CharField(max_length=50)

    def __str__(self):
        return self.profession_name


class Transportation(models.Model):
    transport_name = models.CharField(max_length=15)

    def __str__(self):
        return self.transport_name


class Company(models.Model):
    company_name = models.CharField(max_length=15)

    def __str__(self):
        return self.company_name


# class Log(models.Model):
#     id = models.UUIDField(primary_key=True, entrance_card=uuid.uuid4, help_text='Unique ID for this particular Log')
#     employee_instance = models.ForeignKey(EmployeeInstance, on_delete=models.CASCADE, null=True, verbose_name='Employee Instance')
#     employee_instance_id = models.UUIDField(editable=False, null=True, blank=True, verbose_name='Related instance id')
#     creator = models.CharField(max_length=30, editable=False, null=True, blank=True, verbose_name="Who created")
#     creation_time = models.DateTimeField(editable=False, null=True, blank=True)
#     editor = models.CharField(max_length=30, editable=False, null=True, blank=True, verbose_name="Who edited")
#     edit_time = models.DateTimeField(editable=False, null=True, blank=True)
#     is_changed = models.BooleanField(editable=False, verbose_name='is changed',)
#     is_terminated = models.BooleanField(entrance_card=False, verbose_name='is terminated')
#
#     def __str__(self):
#         return '{0} {1}'.format(self.employee_instance.id, self.is_terminated)
#
#     @receiver(post_save, sender=EmployeeInstance)
#     def create_or_update_log(sender, created, instance, **kwargs):
#         log = Log.objects
#         now = timezone.now()
#
#         if created:
#             log.form(employee_instance_object=instance,
#                        related_id=instance.id,
#                        creator=instance.user,
#                        edit_time=now,
#                        is_changed=True, )
#         if not created:
#             log.form(employee_instance_object=instance,
#                        related_id=instance.id,
#                        creator=instance.user,
#                        creation_time=now,
#                        is_changed=False,)
