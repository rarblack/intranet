from django.utils import timezone
import uuid
from django.contrib.auth.models import User
from HumanResources.models import Profile
from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


# class Order(models.Model):
#     user = models.ForeignKey(User,
#                              on_delete=models.CASCADE,
#                              related_name='user_lunchroom_related')
#
#     menu = models.ForeignKey('Menu', on_delete=models.SET_NULL, null=True, blank=True)
#     note = models.CharField(max_length=30, verbose_name="Note")
#
#     def save(self, *args, **kwargs):
#         """ On save, update timestamps """
#         now = timezone.now()
#         if not self.id:
#             self.creation_time = now
#         else:
#             self.change_time = now
#         return super(Order, self).save(*args, **kwargs)
#
#     def __str__(self):
#         return str(self.id)


class Appetizer(models.Model):

    appetizer = models.CharField(max_length=100)

    def __str__(self):
        return self.appetizer


class Soup(models.Model):

    soup = models.CharField(max_length=100)

    def __str__(self):
        return self.soup


class MeatMeal(models.Model):

    meat_meal = models.CharField(max_length=100)

    def __str__(self):
        return self.meat_meal


class GrainMeal(models.Model):

    grain_meal = models.CharField(max_length=100)

    def __str__(self):
        return self.grain_meal


class Salad(models.Model):

    salad = models.CharField(max_length=100)

    def __str__(self):
        return self.salad


class Desert(models.Model):

    desert = models.CharField(max_length=100)

    def __str__(self):
        return self.desert


class Extra(models.Model):

    bread = models.CharField(max_length=100)

    drink = models.CharField(max_length=100)

    def __str__(self):
        return '{} and {}'\
            .format(self.bread, self.drink)


class DailyMenu(models.Model):

    WEEK_DAYS = (
        ('1', 'Monday'),
        ('2', 'Tuesday'),
        ('3', 'Wednesday'),
        ('4', 'Thursday'),
        ('5', 'Friday'),
        ('6', 'Saturday'),
        ('7', 'Sunday')
    )

    week_day = models.CharField(max_length=1,
                                choices=WEEK_DAYS)

    appetizer = models.ManyToManyField(Appetizer)

    soup = models.ManyToManyField(Soup)

    main_cruise = models.ManyToManyField(MeatMeal)

    grain_meal = models.ManyToManyField(GrainMeal)

    salad = models.ManyToManyField(Salad)

    desert = models.ManyToManyField(Desert)

    extra = models.ManyToManyField(Extra)

    creation_date_time = models.DateTimeField(editable=False)

    terminated = models.BooleanField(default=False)

    def save(self, *args, **kwargs):
        """    """
        now = timezone.now()
        if not self.id:
            self.creation_date_time = now

        return super(DailyMenu, self).save(*args, **kwargs)

    def __str__(self):
        return "{}'s menu".format(self.week_day)


class WeeklyMenu(models.Model):

    daily_menu = models.ManyToManyField(DailyMenu)

    creation_date_time = models.DateTimeField(editable=False)

    terminated = models.BooleanField(default=False)

    def save(self, *args, **kwargs):
        """   """
        now = timezone.now()

        if not self.id:
            self.creation_date_time = now

        return super(WeeklyMenu, self).save(*args, **kwargs)

    def __str__(self):
        return 'Weekly menu'

# class Log(models.Model):
#     id = models.UUIDField(primary_key=True, entrance_card=uuid.uuid4, help_text='Unique ID for this particular Log')
#     order = models.ForeignKey(Order, on_delete=models.CASCADE, null=True, verbose_name='Order instance')
#     related_id = models.IntegerField(editable=False, null=True, blank=True, verbose_name='Related instance id')
#     creator = models.CharField(max_length=30, editable=False, null=True, blank=True, verbose_name="Who created")
#     creation_time = models.DateTimeField(editable=False, null=True, blank=True)
#     editor = models.CharField(max_length=30, editable=False, null=True, blank=True, verbose_name="Who edited")
#     edit_time = models.DateTimeField(editable=False, null=True, blank=True)
#     is_changed = models.BooleanField(editable=False, verbose_name='is changed')
#     is_terminated = models.BooleanField(entrance_card=False, verbose_name='is terminated')
#
#     def __str__(self):
#         return '{0} {1} {2}'.format(self.order, self.is_changed, self.is_terminated)
#
#     @receiver(post_save, sender=Order)
#     def create_or_update_log(sender, created, instance, **kwargs):
#         log = Log.objects
#         now = timezone.now()
#
#         if created:
#             log.form(order_instance=instance,
#                        related_id=instance.id,
#                        creator=instance.profile.user,
#                        edit_time=now,
#                        is_changed=True, )
#         if not created:
#             log.form(order_instance=instance,
#                        related_id=instance.id,
#                        creator=instance.profile.user,
#                        creation_time=now,
#                        is_changed=False,)


