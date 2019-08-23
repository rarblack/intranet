from django.urls import path, re_path
from GuestControl.views.internal.visitor import views

urlpatterns = []

# CREATE
urlpatterns += [
    re_path(r'/create[/]?$',   views.TicketCreateView.as_view(),     name='internal_visitor_ticket_create'),
]

# TEMPLATE
urlpatterns += [
]


# DETAIL
urlpatterns += [
    re_path(r'/detail/(?P<pk>\d+?)[/]$',   views.TicketDetailView.as_view(),   name='internal_visitor_ticket_detail'),
]

# UPDATE
urlpatterns += [
    re_path(r'/update/(?P<pk>\d+?)[/]?$',        views.TicketUpdateView.as_view(),        name='internal_visitor_ticket_update'),
]

# DELETE
urlpatterns += [

]

# LIST
urlpatterns += [
    re_path(r's/list/(?P<pattern>.+?)[/]?$', views.TicketsListView.as_view(),   name='internal_visitor_tickets_list'),
]

# METHOD
urlpatterns += [
    re_path(r'/open/(?P<pk>\d+?)[/]?$',  views.ticket_open_method,  name='internal_visitor_ticket_open'),
    re_path(r'/close/(?P<pk>\d+?)[/]?$', views.ticket_close_method, name='internal_visitor_ticket_close'),
]