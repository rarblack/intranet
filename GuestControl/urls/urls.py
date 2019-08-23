from django.urls import path, re_path
from django.conf.urls import include

from GuestControl.views.navigation import views


urlpatterns = [
    path('/internal/visitor/ticket', include('GuestControl.urls.internal.visitor.urls')),
    path('/external/visitor/ticket', include('GuestControl.urls.external.visitor.urls')),
    path('/external/entrance/card', include('GuestControl.urls.external.entrance_card.urls')),
]


#                                                                                                             NAVIGATION
urlpatterns += [
    re_path(r'/navigation[/]?$',   views.NavigationTemplateView.as_view(), name='navigation_template'),
]
