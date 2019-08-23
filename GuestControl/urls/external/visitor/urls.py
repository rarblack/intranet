from django.urls import path, re_path
from GuestControl.views.external.visitor import views

urlpatterns = []

# CREATE
urlpatterns += [
    re_path(r'/create[/]?$', views.ExternalVisitorTicketCreateView.as_view(), name='external_visitor_ticket_create'),
]

# TEMPLATE
urlpatterns += [
]


# DETAIL
urlpatterns += [
    re_path(r'/detail/(?P<pk>\d+?)[/]$', views.ExternalVisitorTicketDetailView.as_view(), name='external_visitor_ticket_detail'),
]

# UPDATE
urlpatterns += [
    re_path(r'/update/(?P<pk>\d+?)[/]?$', views.ExternalVisitorTicketUpdateView.as_view(), name='external_visitor_ticket_update'),
]

# DELETE
urlpatterns += [

]

# LIST
urlpatterns += [
    re_path(r's/list/(?P<pattern>.+?)]?$', views.ExternalVisitorTicketsListView.as_view(), name='external_visitor_tickets_list'),
]

# METHOD
urlpatterns += [
    re_path(r'/open/(?P<pk>\d+?)[/]?$', views.external_visitor_ticket_open_method, name='external_visitor_ticket_open'),
    re_path(r'/close/(?P<pk>\d+?)[/]?$', views.external_visitor_ticket_close_method, name='external_visitor_ticket_close'),
]