from django.db import models
from django.conf import settings
from django.utils import timezone
from django.urls import reverse_lazy

from .choices import STATUSES, CATEGORIES, PRIORITY_SCALES


def primary_image_directory_path(instance, filename):
    return 'news/main/{0}_{1}/{2}'.format(
        instance.detail.created_by.id,
        instance.detail.created_by.username.upper(),
        filename
    )


def secondary_image_directory_path(instance, filename):
    return 'news/front/{0}_{1}/{2}'.format(
        instance.detail.created_by.id,
        instance.detail.created_by.username.upper(),
        filename
    )


class Tag(models.Model):

    name = models.CharField(max_length=100)

    category = models.IntegerField(choices=CATEGORIES,
                                   default=0)

    description = models.TextField(max_length=300)

    created_by = models.ForeignKey(settings.AUTH_USER_MODEL,
                                   on_delete=models.SET_NULL,
                                   null=True,
                                   related_name='news_tag_created_by')

    created_at = models.DateTimeField(default=timezone.now)

    class Meta:
        verbose_name_plural = 'Tags'

    def __str__(self):
        return '{}'.format(self.name)


class Article(models.Model):

    subject = models.CharField(max_length=100)

    title = models.CharField(max_length=100,
                             null=True)

    introduction = models.TextField(max_length=500,
                                    null=True)

    body = models.TextField(max_length=5000)

    conclusion = models.TextField(max_length=700,
                                  blank=True,
                                  null=True)

    tags = models.ManyToManyField(Tag)

    importance = models.IntegerField(choices=PRIORITY_SCALES,
                                     default=0)

    primary_image = models.ImageField(upload_to=primary_image_directory_path,
                                      null=True,
                                      blank=True,
                                      default=None)

    secondary_image = models.ImageField(upload_to=secondary_image_directory_path,
                                        null=True,
                                        blank=True,
                                        default=None)

    detail = models.OneToOneField('ArticleDetail',
                                  on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = 'Articles'

    def __str__(self):
        return '{}'.format(self.title)

    def get_absolute_path(self):
        return reverse_lazy('news:article_detail', kwargs={'pk': self.pk})


class ArticleDetail(models.Model):
    status = models.IntegerField(choices=STATUSES)

    processed_by = models.ForeignKey(settings.AUTH_USER_MODEL,
                                     on_delete=models.SET_NULL,
                                     null=True,
                                     blank=True,
                                     default=None,
                                     related_name='news_article_detail_processed_by')

    processed_at = models.DateTimeField(null=True,
                                        blank=True,
                                        default=None)

    created_by = models.ForeignKey(settings.AUTH_USER_MODEL,
                                   on_delete=models.SET_NULL,
                                   null=True,
                                   related_name='news_article_detail_created_by')

    created_at = models.DateTimeField(default=timezone.now)

    class Meta:
        verbose_name_plural = 'Articles'

    def __str__(self):
        return 'ID: {0}'.format(self.pk)


class Activity(models.Model):

    detail = models.ForeignKey(ArticleDetail,
                               on_delete=models.CASCADE)

    status = models.IntegerField(choices=STATUSES)

    created_by = models.ForeignKey(settings.AUTH_USER_MODEL,
                                   on_delete=models.SET_NULL,
                                   null=True,
                                   related_name='news_activity_created_by')

    created_at = models.DateTimeField(default=timezone.now)

    class Meta:
        verbose_name_plural = 'Activities'

    def __str__(self):
        return 'ID: {0} Ticket ID: {1}'.format(self.id, self.detail_id)


