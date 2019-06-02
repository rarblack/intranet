from django.urls import re_path
from . import views

# TEMPLATE
urlpatterns = [
    re_path(r'^[/]?$', views.DashboardTemplateView.as_view(), name='dashboard_template')
]