from django.urls import re_path
from . import views

urlpatterns = []

# CREATE
urlpatterns += [
    re_path(r'/create/ticket[/]?$',   views.TicketCreateView.as_view(),     name='ticket_create'),
    re_path(r'/create/car[/]?$', views.CarCreateView.as_view(),   name='car_create')
]

# DETAIL
urlpatterns += [
    re_path(r'/detail/ticket/(?P<pk>\d+?)[/]$',   views.TicketDetailView.as_view(),   name='ticket_detail'),
    re_path(r'/detail/car/(?P<pk>\d+?)[/]$', views.CarDetailView.as_view(), name='car_detail')

]

# UPDATE
urlpatterns += [
    re_path(r'/update/ticket/(?P<pk>\d+?)[/]?$',       views.TicketUpdateView.as_view(),   name='ticket_update'),
    re_path(r'/update/ticketdetail/(?P<pk>\d+?)[/]?$', views.TicketDetailUpdateView.as_view(),  name='ticket_detail_update'),
    re_path(r'/update/car/(?P<pk>\d+?)[/]?$',     views.CarUpdateView.as_view(), name='car_update'),
]

# DELETE
urlpatterns += [

]

# LIST
urlpatterns += [
    re_path(r'/list/(?P<pattern>.+?)/tickets[/]?$', views.TicketsListView.as_view(),   name='tickets_list'),
    re_path(r'/list/cars[/]?$',                views.CarsListView.as_view(), name='cars_list')
]

# METHOD
urlpatterns += [
    re_path(r'/open/ticket/(?P<pk>\d+?)[/]?$', views.ticket_open_method, name='ticket_open'),
    re_path(r'/close/ticket/(?P<pk>\d+?)[/]?$', views.ticket_close_method, name='ticket_close')
]