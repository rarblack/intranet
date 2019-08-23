from django.urls import path, re_path
from GuestControl.views.external.entrance_card import views

urlpatterns = []

# CREATE
urlpatterns += [
    re_path(r'/create[/]?$', views.ExternalEntranceCardCreateView.as_view(), name='entrance_card_create'),
]

# TEMPLATE
urlpatterns += [
    re_path(r'/view/(?P<pk>\d+?)[/]$', views.ExternalEntranceCardTemplateView.as_view(), name='entrance_card_template'),
]


# DETAIL
urlpatterns += [
    re_path(r'/detail/(?P<pk>\d+?)[/]$', views.ExternalEntranceCardDetailView.as_view(), name='entrance_card_detail'),

]

# UPDATE
urlpatterns += [
]

# DELETE
urlpatterns += [

]

# LIST
urlpatterns += [
    re_path(r's/list/[/]$', views.ExternalEntranceCardsListView.as_view(), name='entrance_cards_list'),
]


# METHOD
urlpatterns += [
]