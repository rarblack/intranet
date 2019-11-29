from django.urls import path

from ....views.classes.post.views import PostDetailView, PostsListView
# from ...views.method_based.post.views import

urlpatterns = []

# CLASS BASED
urlpatterns += [
    # path('create/', PostCreateView.as_view(), name='create_post'),
    # path('<int:pk>/update/', PostUpdateView.as_view(), name='update_post'),
    path('<int:pk>/', PostDetailView.as_view(), name='detail_post'),
    path('', PostsListView.as_view(), name='list_posts'),
]

# METHOD BASED
# urlpatterns += [
#     path('open/post/<int:pk>',  views.article_open_method,  name='article_open'),
#     path('close/post/<int:pk>', views.article_close_method, name='article_close')
# ]
