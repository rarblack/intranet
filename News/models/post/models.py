from django.db import models
from django.conf import settings
from django.utils import timezone
from django.urls import reverse_lazy

from ckeditor_uploader.fields import RichTextUploadingField

from ...choices.common.choices import CATEGORIES
from ...choices.post import choices


def upload_image_path(instance, filename):
    return 'news/images/users/{0}/posts/{1}/{2}'.format(
        instance.created_by.id,
        instance.pk,
        filename
    )


class PostModel(models.Model):

    image = models.ImageField(upload_to=upload_image_path)

    title = models.CharField(max_length=100,
                             null=True)

    abstract = models.CharField(
        max_length=1000,
        null=True,
        blank=True
    )

    body = RichTextUploadingField()

    tags = models.ManyToManyField("News.TagModel")

    priority = models.IntegerField(choices=choices.PRIORITY_SCALES,
                                   default=0)

    category = models.IntegerField(choices=CATEGORIES,
                                   default=0)

    created_by = models.ForeignKey(settings.AUTH_USER_MODEL,
                                   on_delete=models.SET_NULL,
                                   null=True,
                                   related_name='news_post_created_by')

    created_at = models.DateTimeField(default=timezone.now)

    class Meta:
        verbose_name = 'Post'
        verbose_name_plural = 'Posts'

    def __str__(self):
        return '{0}'.format(self.title)

    def get_absolute_path(self):
        return reverse_lazy('news:detail_post', kwargs={'pk': self.pk})

