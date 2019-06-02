from django.urls import re_path, path
from . import views


urlpatterns = [
    re_path(r'', views.pob, name='pob'),
    re_path(r'/table[/]?$', views.view_table, name='table'),
    re_path(r'/table/add[/]?$', views.addEmployeeInstance, name='add'),
]

urlpatterns += [
    re_path(r'/update[/]?$', views.view_update, name='update'),
    path('/update/<uuid:pk>', views.update_employee_instance, name='update-employee-instance'),
]
