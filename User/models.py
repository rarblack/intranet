from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
from django.utils.translation import gettext, gettext_lazy as _
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import AbstractUser

from . import choices


def upload_image_path(instance, filename):
    return "/media/users/{0}/profile-images/{1}".format(
        instance.created_by.id,
        filename
    )


class Profile(models.Model):

    profile_image = models.ImageField(
        upload_to=upload_image_path,
        null=True
    )

    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
    )

    bio = models.TextField(
        max_length=250,
        blank=True,
        null=True
    )

    middle_name = models.CharField(
        max_length=30,
        blank=True
    )

    birth_date = models.DateField(null=True)

    gender = models.IntegerField(
        choices=choices.GENDERS,
        null=True,
        default=0
    )

    employ_date = models.DateTimeField(null=True)

    mobile_number = models.CharField(
        max_length=150,
        null=True
    )

    internal_number = models.CharField(
        max_length=150,
        null=True
    )

    department = models.IntegerField(
        choices=choices.DEPARTMENTS,
        null=True
    )

    balance = models.FloatField(default=0)

    created_at = models.DateTimeField(auto_now_add=True)

    created_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        related_name='hr_profile_created_by'
    )

    def __str__(self):
        return self.user.username

    def get_full_name(self):
        return f'{self.user.first_name} {self.user.last_name}'

    def get_balance(self):
        return self.balance

    def get_creator(self):
        return self.created_by

    @receiver(post_save, sender=User)
    def create_or_update_user_account(sender, instance, created, **kwargs):
        if created:
            Profile.objects.create(user=instance, created_by=instance)
        instance.profile.save()


