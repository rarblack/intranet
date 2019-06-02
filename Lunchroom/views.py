from django.shortcuts import render
from . import models
from django.views import generic


class WeeklyMenusView(generic.ListView):
    model = models.WeeklyMenu
    context_object_name = 'menus'
    template_name = 'lunchroom/weekly-menus_list.html'


class DailyMenuView(generic.DetailView):
    model = models.DailyMenu
    context_object_name = 'menu'
    template_name = 'lunchroom/daily_menu_detail.html'


def daily_menu(request):

    queryset = models.DailyMenu.objects.all()

    context = {
        'queryset': queryset,
    }

    return render(request,
                  'lunchroom/lunch_profile.html',
                  context=context, )




def weekly_menu(request):

    queryset = models.WeeklyMenu.objects.all()

    context = {
        'queryset': queryset,
    }

    return render(request,
                  'lunchroom/weekly-menus_list.html',
                  context=context, )

