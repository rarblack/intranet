from django.urls import re_path
from . import views

urlpatterns = [
    re_path('', views.TestsView.as_view(), name='view-test')
]