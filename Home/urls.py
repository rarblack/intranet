from django.urls import path, re_path
from . import views

urlpatterns = []

# TEMPLATE
urlpatterns += [
    re_path(r'', views.HomeTemplateView.as_view(), name='home_template')
]