from django.db import models
from django.conf import settings
from django.utils import timezone

from ...choices.tag import choices


class TagModel(models.Model):

    name = models.CharField(max_length=100)

    description = models.TextField(max_length=300)

    category = models.IntegerField(choices=choices.CATEGORIES,
                                   default=0)

    created_by = models.ForeignKey(settings.AUTH_USER_MODEL,
                                   on_delete=models.SET_NULL,
                                   null=True,
                                   related_name='news_tag_created_by')

    created_at = models.DateTimeField(default=timezone.now)

    class Meta:
        verbose_name = 'Tag'
        verbose_name_plural = 'Tags'

    def __str__(self):
        return '{0}'.format(self.name)
