from django.urls import re_path
from . import views

urlpatterns = []

# CREATE
urlpatterns += [
    re_path(r'/create/ticket[/]?$',   views.TicketCreateView.as_view(),     name='ticket_create'),
    re_path(r'/create/material[/]?$', views.MaterialCreateView.as_view(),   name='material_create')
]

# DETAIL
urlpatterns += [
    re_path(r'/detail/ticket/(?P<pk>\d+?)[/]$',   views.TicketDetailView.as_view(),   name='ticket_detail'),
    re_path(r'/detail/material/(?P<pk>\d+?)[/]$', views.MaterialDetailView.as_view(), name='material_detail')

]

# UPDATE
urlpatterns += [
    re_path(r'/update/ticket/(?P<pk>\d+?)[/]?$',       views.TicketUpdateView.as_view(),   name='ticket_update'),
    re_path(r'/update/ticketdetail/(?P<pk>\d+?)[/]?$', views.TicketDetailUpdateView.as_view(),  name='ticket_detail_update'),
    re_path(r'/update/material/(?P<pk>\d+?)[/]?$',     views.MaterialUpdateView.as_view(), name='material_update'),
]

# DELETE
urlpatterns += [

]

# LIST
urlpatterns += [
    re_path(r'/list/(?P<pattern>.+?)/tickets[/]?$', views.TicketsListView.as_view(),   name='tickets_list'),
    re_path(r'/list/materials[/]?$',                views.MaterialsListView.as_view(), name='materials_list')
]

# METHOD
urlpatterns += [
    re_path(r'/open/ticket/(?P<pk>\d+?)[/]?$', views.ticket_open_method, name='ticket_open'),
    re_path(r'/close/ticket/(?P<pk>\d+?)[/]?$', views.ticket_close_method, name='ticket_close')
]