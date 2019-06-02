from django.contrib import admin
from Lunchroom.models import Appetizer, Soup, MeatMeal, GrainMeal, Salad, Desert, Extra, DailyMenu, WeeklyMenu


@admin.register(Appetizer)
class AppetizerAdmin(admin.ModelAdmin):
    list_display = ('id', 'appetizer')


@admin.register(Soup)
class SoupAdmin(admin.ModelAdmin):
    list_display = ('id', 'soup')


@admin.register(MeatMeal)
class MeatMealAdmin(admin.ModelAdmin):
    list_display = ('id', 'meat_meal')


@admin.register(GrainMeal)
class GrainMealAdmin(admin.ModelAdmin):
    list_display = ('id', 'grain_meal')


@admin.register(Salad)
class SaladAdmin(admin.ModelAdmin):
    list_display = ('id', 'salad')


@admin.register(Desert)
class DesertAdmin(admin.ModelAdmin):
    list_display = ('id', 'desert')


@admin.register(Extra)
class ExtraAdmin(admin.ModelAdmin):
    list_display = ('id', 'bread', 'drink')


@admin.register(DailyMenu)
class DailyMenuAdmin(admin.ModelAdmin):
    list_display = ('id', 'get_week_day_display')


@admin.register(WeeklyMenu)
class WeeklyMenuAdmin(admin.ModelAdmin):
    display = 'daily_menu'


# @admin.register(Log)
# class LogAdmin(admin.ModelAdmin):
#     list_display = ('id', 'editor', 'creator', 'is_changed',)

