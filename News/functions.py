from django.utils import timezone
from datetime import timedelta
import random

from News.models import Article
from HumanResources.models import Profile


def articles_latest(how_many=5):
    """
    This method is to return retrieve declared sized latest posts to the template. Additionally it applies sorting to
    the queryset before slice.

    :param model:
    :param how_many: default is 4 and defines size of return queryset
    :return: sorted(model.objects.all(), key=lambda e: e.created_at, reverse=True) method sorts all model
    instances according to the created_at key in descend order. [:how_many] slices instances till how_many index.
    """
    all_articles = Article.objects.select_related('detail').all()
    sorted_articles_desc = sorted(all_articles, key=lambda e: e.detail.created_at, reverse=True)
    latest_articles = sorted_articles_desc[:how_many]

    return latest_articles


def employees_closest_birthdays():
    today = timezone.now()
    birthdays = Profile.objects.filter(birth_date=today.date())
    birthdays_len = len(birthdays)
    if birthdays:
        if birthdays_len >= 2:
            random_indexes = random.sample(range(0, birthdays_len), 2)
            return [[birthdays[random_indexes[1]], birthdays[random_indexes[0]]], range(0)]

        elif birthdays_len == 1:
            return [[birthdays[0]], range(1)]
    else:
        return [[], range(2)]


def employees_newest(how_many=2):
    """
    This method is to retrieve a random at today's date entered employee.

    :param model: from which model the new_employees queryset will be gathered
    :return: random new employee

    """
    today = timezone.now()
    employees = Profile.objects.filter(employ_date__gte=today.date()-timedelta(7))
    employees_len = len(employees)
    if employees:
        if employees_len >= 3:
            random_indexes = random.sample(range(0, employees_len), 3)
            return [[employees[random_indexes[2]], employees[random_indexes[1]], employees[random_indexes[0]]], range(0)]

        elif employees_len == 2:
            random_indexes = random.sample(range(0, employees_len), 2)
            return [[employees[random_indexes[2]], employees[random_indexes[1]]], range(1)]

        elif employees_len == 1:
            return [[employees[0]], range(2)]
    else:
        return [[], range(3)]

