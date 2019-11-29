from django.urls import re_path
from User import views

# make-visitor-request.html
urlpatterns = [
    re_path(r'', views.hr, name='hr'),
]

# # response.html
# urlpatterns += [
#     path('response/', views.list_orders, name='response'),
#     path('response/reject/<int:pk>/', views.reject, name='reject'),
#     path('response/accept/<int:pk>/', views.accept_and_response, name='accept'),
# ]
