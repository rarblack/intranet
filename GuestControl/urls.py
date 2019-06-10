from django.urls import path, re_path
from . import views

urlpatterns = []

# CREATE
urlpatterns += [
    re_path(r'/create/external-visit-ticket[/]?$',   views.ExternalVisitTicketCreateView.as_view(),     name='external_visit_ticket_create'),
    re_path(r'/create/internal-visit-ticket[/]?$',   views.InternalVisitTicketCreateView.as_view(),     name='internal_visit_ticket_create'),
    re_path(r'/create/visitor-entrance-card[/]?$',   views.VisitorEntranceCardCreateView.as_view(),     name='visitor_entrance_card_create'),
]

# TEMPLATE
urlpatterns += [
    re_path(r'/view/visitor-entrance-card/(?P<pk>\d+?)[/]$',   views.VisitorEntranceCardTemplateView.as_view(),     name='visitor_entrance_card_template'),
]


# DETAIL
urlpatterns += [
    re_path(r'/detail/external-visit-ticket/(?P<pk>\d+?)[/]$',   views.ExternalVisitTicketDetailView.as_view(),   name='external_visit_ticket_detail'),
    re_path(r'/detail/internal-visit-ticket/(?P<pk>\d+?)[/]$',   views.InternalVisitTicketDetailView.as_view(),   name='internal_visit_ticket_detail'),
    re_path(r'/detail/visitor-entrance-card/(?P<pk>\d+?)[/]$',   views.VisitorEntranceCardDetailView.as_view(),   name='visitor_entrance_card_detail'),

]

# UPDATE
urlpatterns += [
    re_path(r'/update/external-visit-ticket/(?P<pk>\d+?)[/]?$',        views.ExternalVisitTicketUpdateView.as_view(),        name='external_visit_ticket_update'),
    re_path(r'/update/internal-visit-ticket/(?P<pk>\d+?)[/]?$',        views.InternalVisitTicketUpdateView.as_view(),        name='internal_visit_ticket_update'),
    # re_path(r'/update/external-visit-ticket-detail/(?P<pk>\d+?)[/]?$', views.ExternalVisitTicketDetailUpdateView.as_view(),  name='external_visit_ticket_detail_update'),
    # re_path(r'/update/internal-visit-ticket-detail/(?P<pk>\d+?)[/]?$', views.InternalVisitTicketDetailUpdateView.as_view(),  name='internal_visit_ticket_detail_update'),
]

# DELETE
urlpatterns += [

]

# LIST
urlpatterns += [
    re_path(r'/list/(?P<pattern>.+?)/external-visit-tickets[/]?$', views.ExternalVisitTicketsListView.as_view(),   name='external_visit_tickets_list'),
    re_path(r'/list/(?P<pattern>.+?)/internal-visit-tickets[/]?$', views.InternalVisitTicketsListView.as_view(),   name='internal_visit_tickets_list'),
    re_path(r'/list/visitor-entrance-cards[/]$',   views.VisitorEntranceCardsListView.as_view(),            name='visitor_entrance_cards_list'),
]

# METHOD
urlpatterns += [
    re_path(r'/open/external_visit_ticket/(?P<pk>\d+?)[/]?$',  views.external_visit_ticket_open_method,  name='external_visit_ticket_open'),
    re_path(r'/close/external_visit_ticket/(?P<pk>\d+?)[/]?$', views.external_visit_ticket_close_method, name='external_visit_ticket_close'),
    re_path(r'/open/internal_visit_ticket/(?P<pk>\d+?)[/]?$',  views.internal_visit_ticket_open_method,  name='internal_visit_ticket_open'),
    re_path(r'/close/internal_visit_ticket/(?P<pk>\d+?)[/]?$', views.internal_visit_ticket_close_method, name='internal_visit_ticket_close'),
]