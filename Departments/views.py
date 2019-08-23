from django.shortcuts import render
from django.contrib.auth import mixins
from django.views import generic
from django.urls import reverse_lazy
from django.utils import timezone

from datetime import datetime

from . import models


#    _navigation_


#    DRILLING


#                                                                                                                 CREATE
# WELL DATA STATISTIC CREATE VIEW
class WellDataStatCreateView(mixins.LoginRequiredMixin, generic.CreateView):
    model = models.WellDataStatModel
    fields = ('subject', 'association_date', 'image', 'description')
    template_name = 'drilling/well_data_statistics/create/well_data_stat_create.html'
    success_url = reverse_lazy('department:drilling_well_data_stat_list')

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.creator = self.request.user
        self.object.save()
        return super().form_valid(form)


#                                                                                                                   LIST
# WELL DATA STATISTICS LIST VIEW
class WellDataStatsListView(mixins.LoginRequiredMixin, generic.ListView):
    model = models.WellDataStatModel
    context_object_name = 'stats'
    template_name = 'drilling/well_data_statistics/list/well_data_stats_list.html'

    def post(self, request, *args, **kwargs):
        stats = self.model.objects.filter(association_date__gte=self.request.POST['start_date'],
                                          association_date__lte=self.request.POST['end_date'])
        return render(request, 'drilling/well_data_statistics/list/well_data_stats_list.html',
                      context={'stats': stats} )

    def get_queryset(self):
        print(timezone.now())
        return self.model.objects.filter(association_date=timezone.now())


#                                                                                                               TEMPLATE
# _navigation_ TEMPLATE VIEW
class NavigationTemplateView(mixins.LoginRequiredMixin, generic.TemplateView):
    template_name = 'drilling/template/navigation/navigation_template.html'
