from django.urls import path, re_path
from . import views

# VIEW
urlpatterns = [
    re_path(r'/view/uploaded/files[/]?$', views.ListViewFilesView.as_view(), name='view-uploaded-files')
]

# UPLOAD
urlpatterns += [
    re_path('/upload/files[/]?$', views.FileCreateView.as_view(), name='upload-files')
]

# DELETE
urlpatterns += [
    re_path('/delete/file/<int:pk>[/]?$', views.DeleteUploadFilesView.as_view(), name='delete-uploaded-file')
]


# DOWNLOAD
urlpatterns += [
    re_path(r'/download/file/(?P<path>.*?)[/]?$', views.download, name='download-uploaded-file')
]