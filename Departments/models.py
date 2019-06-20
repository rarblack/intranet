from django.db import models
from django.utils import timezone
from django.conf import settings


# DRILLING
#                                                                                                      FILE UPLOAD PATHS
def upload_image_to(instance, filename):
    return f'departments/drilling/{filename}'


#                                                                                                               ABSTRACT
class DetailAbstractModel(models.Model):

    creation_datetime = models.DateTimeField(default=timezone.now,
                                             verbose_name='Creation time')

    class Meta:
        abstract = True


#                                                                                                               DRILLING
# WELL DATA MODEL
class WellStatisticalDataModel(DetailAbstractModel):

    image = models.ImageField(upload_to=upload_image_to)

    subject = models.CharField(max_length=500,
                               null=True,
                               blank=True,
                               verbose_name='Subject of the instance.')

    description = models.TextField(max_length=10000,
                                   null=True,
                                   blank=True,
                                   verbose_name='Description of the instance.')

    creator = models.ForeignKey(settings.AUTH_USER_MODEL,
                                null=True,
                                on_delete=models.SET_NULL,
                                verbose_name='Creator',
                                related_name='departments_drilling_wellStatisticalDataModel_creator')

    def __str__(self):
        return self.subject

