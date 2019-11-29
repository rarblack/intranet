# from django.shortcuts import get_object_or_404
# from django.http import HttpResponseRedirect
# from django.db.models import Q
from django.views.generic import ListView, DetailView
# from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin

from ....models.post import models


class PostsListView(LoginRequiredMixin, ListView):
    model = models.PostModel
    template_name = 'news/post/list/posts-list.html'
    context_object_name = 'posts'
    paginate_by = 9
    queryset = models.PostModel.objects.all().order_by('-created_at')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        count = self.queryset.count()

        if count > 4:
            context['latest_posts'] = self.queryset[:4]
            context['oldest_posts'] = self.queryset[:count-4:-1]
        else:
            context['latest_posts'] = self.queryset
            context['oldest_posts'] = self.queryset
        return context


class PostDetailView(LoginRequiredMixin, DetailView):
    model = models.PostModel
    context_object_name = 'post'
    template_name = 'news/post/detail/post-detail.html'

    def get_author_all_posts_count(self):
        posts = self.model.objects.filter(created_by=self.request.user).order_by('-created_at')
        count = posts.count()
        return posts, count

    def get_author_5_latest_posts(self):
        posts, count = self.get_author_all_posts_count()
        if count > 5:
            return posts[:5]
        return posts

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['author_recent_posts'] = self.get_author_5_latest_posts()
        return context
