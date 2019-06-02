from django.urls import re_path
from . import views


urlpatterns = [
    re_path(r'', views.WeeklyMenusView.as_view(), name='view-weekly-menu'),
]

urlpatterns += [
    re_path(r'/daily', views.DailyMenuView.as_view(), name='view-daily-menu')
]
