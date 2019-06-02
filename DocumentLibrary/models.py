from django.db import models
from django.conf import settings
from django.contrib.auth.models import User


def user_file_path(instance, filename):
    return 'Document Library/{0}/{1} {2}/{3}'.format(
        instance.created_by.id,
        instance.created_by.profile.get_department_display(),
        instance.created_by.username.upper(),
        filename
    )


class UploadFiles(models.Model):

    file = models.FileField(upload_to=user_file_path)

    file_name = models.CharField(max_length=300,
                                 null=True)

    file_extension = models.CharField(max_length=30)

    belonged_department = models.IntegerField()

    created_at = models.DateTimeField(auto_now_add=True,
                                      editable=False)
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL,
                                   on_delete=models.SET_NULL,
                                   null=True,
                                   editable=False)
