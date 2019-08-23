from django.urls import path, re_path
from . import views


urlpatterns = []


#                                                                                                                 CREATE
urlpatterns += [
    re_path(r'/drilling/create/well-data-stat[/]?$', views.WellDataStatCreateView.as_view(), name='drilling_well_data_stat_create')
]

#                                                                                                                   LIST
urlpatterns += [
    re_path(r'/drilling/list/well-data-stats[/]?$', views.WellDataStatsListView.as_view(), name='drilling_well_data_stat_list')
]

#                                                                                                               TEMPLATE
urlpatterns += [
    re_path(r'/drilling/_navigation_[/]?$', views.NavigationTemplateView.as_view(), name='drilling_navigation_template')
]