from django.conf.urls import include
from django.urls import path

urlpatterns = []

urlpatterns += [
    path('posts/', include('News.urls.includes.post.urls')),
]
