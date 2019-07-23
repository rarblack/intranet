from django.db import models
from django.conf import settings
from HumanResources import choices
from django.utils import timezone
from django.contrib.auth.models import User


def upload_to(instance, filename):

    # return f'document_library/department_{instance.creator.profile.department}/user_{instance.creator.profile.id}/{filename}'
    return f'document_library/{filename}'


class DocumentModel(models.Model):

    file = models.FileField(upload_to=upload_to)

    file_name = models.CharField(max_length=300,
                                 null=True)

    file_extension = models.CharField(max_length=30)

    department_belonged = models.IntegerField(choices=choices.DEPARTMENTS,
                                              null=True,
                                              blank=True)

    creator = models.ForeignKey(settings.AUTH_USER_MODEL,
                                on_delete=models.SET_NULL,
                                null=True,
                                editable=False)

    creation_datetime = models.DateTimeField(default=timezone.now,
                                             editable=False)
