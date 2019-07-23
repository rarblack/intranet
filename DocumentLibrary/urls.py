from django.urls import path, re_path
from . import views

# VIEW
urlpatterns = [
    # re_path(r'/list/documents/(?P<table>.*?)[/]?$', views.DocumentsListView.as_view(), name='documents_list')
    re_path(r'/list/documents/[/]?$', views.DocumentsListView.as_view(), name='documents_list'),
    re_path(r'/navigation[/]?$', views.NavigationTemplateView.as_view(), name='navigation_template')
]

# UPLOAD
urlpatterns += [
    re_path('/create/document[/]?$', views.DocumentCreateView.as_view(), name='document_create')
]

# DELETE
urlpatterns += [
    re_path('r/delete/document/(?P<pk>\d+?)[/]?$', views.DeleteDocumentView.as_view(), name='document_delete')
]


# DOWNLOAD
urlpatterns += [
    re_path(r'/download/document/(?P<path>.*?)[/]?$', views.document_download_method, name='document_download')
]