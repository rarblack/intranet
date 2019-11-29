# from django.shortcuts import get_object_or_404
# from django.http import HttpResponseRedirect
# from django.db.models import Q
# from django.views.generic import CreateView, UpdateView, DeleteView, ListView, DetailView, TemplateView
# from django.urls import reverse_lazy
# from django.contrib.auth.mixins import LoginRequiredMixin
# from django.utils import timezone
#
# from .models import Tag, Article, Activity
# from .forms import ArticleCreateModelForm, ArticleUpdateModelForm
# from .functions import  articles_latest, employees_closest_birthdays, employees_newest
#
#
# def article_close_method(request, pk):
#     Activity.objects.create(detail=detail,
#                             status=detail.status,
#                             created_by=detail.processed_by,
#                             created_at=detail.processed_at)
#     detail.status = 4
#     detail.save()
#
#     return HttpResponseRedirect(reverse_lazy('news:articles_list', kwargs={'pattern': 'my/closed'}))
#
#
# def article_open_method(request, pk):
#     detail = get_object_or_404(ArticleDetail, pk=pk)
#     Activity.objects.create(detail=detail,
#                             status=detail.status,
#                             created_by=detail.processed_by,
#                             created_at=detail.processed_at)
#     detail.status = 0
#     detail.save()
#
#     return HttpResponseRedirect(reverse_lazy('news:articles_list', kwargs={'pattern': 'my/open'}))