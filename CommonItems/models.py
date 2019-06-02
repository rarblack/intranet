from django.db import models
from django.utils import timezone
from django.conf import settings


class WorkArea(models.Model):
    name = models.CharField(max_length=50,
                            help_text='Area name such as: PLT11, PLT7 and etc.')

    is_active = models.BooleanField(default=True,
                                    verbose_name='Active')

    created_by = models.ForeignKey(settings.AUTH_USER_MODEL,
                                   on_delete=models.SET_NULL,
                                   null=True,
                                   related_name='commonitems_workarea_created_by')

    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return '{0}'.format(self.name)