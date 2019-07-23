from django.shortcuts import get_object_or_404
from django.http import HttpResponseRedirect
from django.db.models import Q
from django.views.generic import CreateView, UpdateView, DeleteView, ListView, DetailView, TemplateView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.utils import timezone

from .models import Tag, Article, ArticleDetail, Activity
from .forms import ArticleCreateModelForm, ArticleUpdateModelForm
from .functions import  articles_latest, employees_closest_birthdays, employees_newest


class TagCreateView(LoginRequiredMixin, CreateView):
    model = Tag
    fields = ['name', 'category', 'description']
    template_name = 'news/create/tag/tag_create.html'

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.created_by = self.request.user
        self.object.created_at = timezone.now()
        self.object.save()
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["latest_articles"] = articles_latest()
        context["closest_birthdays"] = employees_closest_birthdays()
        context["newest_employees"] = employees_newest()
        return context

    def get_success_url(self):
        return reverse_lazy('news:tag_detail', kwargs={'pk': self.object.pk})


class ArticleCreateView(LoginRequiredMixin, CreateView):
    model = Article
    form_class = ArticleCreateModelForm
    template_name = 'news/create/article/article_create.html'

    def form_valid(self, form):
        detail = ArticleDetail.objects.create(status=0,
                                              created_by=self.request.user,
                                              created_at=timezone.now())
        Activity.objects.create(detail=detail,
                                status=detail.status,
                                created_by=detail.created_by,
                                created_at=detail.created_at)
        self.object = form.save(commit=False)
        self.object.primary_image = self.request.FILES['primary_image']
        self.object.secondary_image = self.request.FILES['secondary_image']
        self.object.detail = detail
        print('Successs')
        self.object.save()
        print('Successs')
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('news:article_detail', kwargs={'pk': self.object.pk})


#                                                                                                                 UPDATE
# ARTICLE UPDATE VIEW
class ArticleUpdateView(LoginRequiredMixin, UpdateView):
    model = Article
    form_class = ArticleUpdateModelForm
    template_name = 'news/update/article/article_update.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["latest_articles"] = articles_latest()
        context["closest_birthdays"] = employees_closest_birthdays()
        context["newest_employees"] = employees_newest()
        return context

    def get_success_url(self):
        return reverse_lazy('news:article_detail', kwargs={'pk': self.object.pk})


# ARTICLE DETAIL UPDATE VIEW
class ArticleDetailUpdateView(LoginRequiredMixin, UpdateView):
    model = ArticleDetail
    fields = ['status']
    template_name = 'news/update/article_detail/article_detail_update.html'

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.processed_by = self.request.user
        self.object.processed_at = timezone.now()
        self.object.save()
        Activity.objects.create(detail=self.object,
                                status=self.object.status,
                                created_by=self.object.processed_by,
                                created_at=self.object.processed_at)
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["latest_articles"] = articles_latest()
        context["closest_birthdays"] = employees_closest_birthdays()
        context["newest_employees"] = employees_newest()
        return context

    def get_success_url(self):
        return reverse_lazy('news:article_detail', kwargs={'pk': self.kwargs.get('pk')})


# TAG UPDATE VIEW
class TagUpdateView(LoginRequiredMixin, UpdateView):
    model = Tag
    fields = ['name', 'category', 'description']
    template_name = 'news/update/tag/tag_update.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["latest_articles"] = articles_latest()
        context["closest_birthdays"] = employees_closest_birthdays()
        context["newest_employees"] = employees_newest()
        return context


#                                                                                                                   LIST
# ARTICLE LIST VIEW
class ArticlesListView(LoginRequiredMixin, ListView):
    model = Article
    template_name = 'news/list/articles/articles_list.html'
    context_object_name = 'articles'

    def get_queryset(self):
        self.pattern = self.kwargs.get('pattern')
        if self.pattern == 'my/open':
            return self.model.objects.select_related('detail').filter(detail__status=0,
                                                                      detail__created_by=self.request.user)

        elif self.pattern == 'my/closed':
            return self.model.objects.select_related('detail').filter(detail__status=4,
                                                                      detail__created_by=self.request.user)

        elif self.pattern == 'by/me/closed':
            return self.model.objects.select_related('detail').filter(detail__status=4,
                                                                      detail__processed_by=self.request.user)
        elif self.pattern == 'by/me/closed':
            return self.model.objects.select_related('detail').filter(detail__status=0,
                                                                      detail__processed_by=self.request.user)

        elif self.pattern == 'all/open':
            return self.model.objects.select_related('detail').filter(~Q(detail__created_by=self.request.user),
                                                                      detail__status=0)

        elif self.pattern == 'all/closed':
            return self.model.objects.select_related('detail').filter(detail__status=4)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["latest_articles"] = articles_latest()
        context["closest_birthdays"] = employees_closest_birthdays()
        context["newest_employees"] = employees_newest()
        return context


#   TAGS LIST VIEW
class TagsListView(LoginRequiredMixin, ListView):
    model = Tag
    template_name = 'news/list/tags/tags_list.html'
    context_object_name = 'tags'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["latest_articles"] = articles_latest()
        context["closest_birthdays"] = employees_closest_birthdays()
        context["newest_employees"] = employees_newest()
        return context


#                                                                                                                 DETAIL
# ARTICLE DETAIL VIEW
class ArticleDetailView(LoginRequiredMixin, DetailView):
    model = Article
    context_object_name = 'article'
    template_name = 'news/detail/article/article_detail.html'

    def get_queryset(self):
        return self.model.objects.select_related('detail').all()


# TAG DETAIL VIEW
class TagDetailView(LoginRequiredMixin, DetailView):
    model = Tag
    template_name = 'news/detail/tag/tag_detail.html'
    context_object_name = 'tag'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["latest_articles"] = articles_latest()
        context["closest_birthdays"] = employees_closest_birthdays()
        context["newest_employees"] = employees_newest()
        return context


#                                                                                                               TEMPLATE
# ARTICLE TEMPLATE VIEW
class ArticleTemplateView(LoginRequiredMixin, TemplateView):
    model = Article
    template_name = 'news/template/article/article_template.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["article"] = get_object_or_404(Article, pk=self.kwargs.get('pk'))
        context["latest_articles"] = articles_latest()
        context["closest_birthdays"] = employees_closest_birthdays()
        context["newest_employees"] = employees_newest()
        return context


#                                                                                                                 DELETE
# TAG DELETE VIEW
class TagDeleteView(LoginRequiredMixin, DeleteView):
    model = Tag
    context_object_name = 'tag'
    template_name = 'news/delete/tag/tag_confirm_delete.html'
    success_url = reverse_lazy('news:tags_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["latest_articles"] = articles_latest()
        context["closest_birthdays"] = employees_closest_birthdays()
        context["newest_employees"] = employees_newest()
        return context


#                                                                                                                METHODS
# ARTICLE DETAIL CLOSE METHOD
def article_close_method(request, pk):
    detail = get_object_or_404(ArticleDetail, pk=pk)
    Activity.objects.create(detail=detail,
                            status=detail.status,
                            created_by=detail.processed_by,
                            created_at=detail.processed_at)
    detail.status = 4
    detail.save()

    return HttpResponseRedirect(reverse_lazy('news:articles_list', kwargs={'pattern': 'my/closed'}))


# ARTICLE DETAIL CLOSE METHOD
def article_open_method(request, pk):
    detail = get_object_or_404(ArticleDetail, pk=pk)
    Activity.objects.create(detail=detail,
                            status=detail.status,
                            created_by=detail.processed_by,
                            created_at=detail.processed_at)
    detail.status = 0
    detail.save()

    return HttpResponseRedirect(reverse_lazy('news:articles_list', kwargs={'pattern': 'my/open'}))