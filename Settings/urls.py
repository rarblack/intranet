from django.urls import re_path
from . import views

urlpatterns = [
    re_path(r'/change-password[/]?$', views.change_password, name='change_password')
]