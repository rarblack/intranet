from django.urls import re_path, path
from Directory import views


urlpatterns = [
    re_path(r"^$|[/]$", views.ContactsListView.as_view(), name='contacts_list')
]