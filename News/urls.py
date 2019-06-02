from django.urls import re_path
from . import views

urlpatterns = []

# CREATE
urlpatterns += [
    re_path(r'/create/article[/]?$',   views.ArticleCreateView.as_view(), name='article_create'),
    re_path(r'/create/tag[/]?$',       views.TagCreateView.as_view(),     name='tag_create')
]

# DETAIL
urlpatterns += [
    re_path(r'/detail/article/(?P<pk>\d+?)[/]$',   views.ArticleDetailView.as_view(), name='article_detail'),
    re_path(r'/detail/tag/(?P<pk>\d+?)[/]$',       views.TagDetailView.as_view(),     name='tag_detail')
]

# UPDATE
urlpatterns += [
    re_path(r'/update/article/(?P<pk>\d+?)[/]?$',       views.ArticleUpdateView.as_view(),       name='article_update'),
    re_path(r'/update/articledetail/(?P<pk>\d+?)[/]?$', views.ArticleDetailUpdateView.as_view(), name='article_detail_update'),
    re_path(r'/update/tag/(?P<pk>\d+?)[/]?$',           views.TagUpdateView.as_view(),           name='tag_update'),
]

# DELETE
urlpatterns += [
    re_path(r'/delete/tag/(?P<pk>\d+?)[/]?$',           views.TagDeleteView.as_view(),           name='tag_delete'),
]

# LIST
urlpatterns += [
    re_path(r'/list/(?P<pattern>.+?)/articles[/]?$', views.ArticlesListView.as_view(), name='articles_list'),
    re_path(r'/list/tags[/]?$',                      views.TagsListView.as_view(),     name='tags_list')
]

# TEMPLATE
urlpatterns += [
    re_path(r'/template/article/(?P<pk>\d+?)[/]$',   views.ArticleTemplateView.as_view(), name='article_template'),
]

# METHOD
urlpatterns += [
    re_path(r'/open/article/(?P<pk>\d+?)[/]?$',  views.article_open_method,  name='article_open'),
    re_path(r'/close/article/(?P<pk>\d+?)[/]?$', views.article_close_method, name='article_close')
]