from django.db.models import Q
from django.http import HttpResponseRedirect
from django.views.generic import CreateView, UpdateView, DeleteView, TemplateView, ListView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy
from django.utils import timezone

from HelpDesk.models import Ticket, TicketDetail, Activity, Message
from News.functions import articles_latest, employees_newest, employees_closest_birthdays


#                                                                                                                 CREATE
# TICKET CREATE VIEW
class TicketCreateView(LoginRequiredMixin, CreateView):
    model = Ticket
    fields = ['type', 'subject', 'location', 'importance', 'note']
    template_name = 'help_desk/default/create/ticket_create.html'
    success_url = reverse_lazy('helpdesk:tickets_list', kwargs={'pattern': 'my/open'})

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["latest_articles"] = articles_latest()
        context["closest_birthdays"] = employees_closest_birthdays()
        context["newest_employees"] = employees_newest()
        return context

    def form_valid(self, form):
        detail = TicketDetail.objects.create(status=0,
                                             created_by=self.request.user)
        Activity.objects.create(detail=detail,
                                status=detail.status,
                                assignee=detail.assignee,
                                created_by=detail.created_by,
                                created_at=detail.created_at)
        self.object = form.save(commit=False)
        self.object.file = self.request.FILES['file']
        self.object.detail = detail
        self.object.save()
        return super().form_valid(form)


#                                                                                                                 UPDATE
class TicketUpdateView(LoginRequiredMixin, UpdateView):
    model = Ticket
    fields = ['type', 'subject', 'location', 'importance', 'note', 'file']
    template_name = 'help_desk/default/update/ticket_update.html'

    def get_success_url(self):
        return reverse_lazy('helpdesk:ticket_detail', kwargs={'pk': self.kwargs.get('pk')})


class TicketDetailUpdateView(LoginRequiredMixin, UpdateView):
    model = TicketDetail
    fields = ['status', 'assignee']
    template_name = 'help_desk/help_desk/update/ticket_detail/ticket_detail_update.html'

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.processed_by = self.request.user
        self.object.processed_at = timezone.now()
        self.object.save()
        Activity.objects.create(detail=self.object,
                                status=self.object.status,
                                assignee=self.object.assignee,
                                created_by=self.object.processed_by,
                                created_at=self.object.processed_at)
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('transportation:ticket_detail', kwargs={'pk': self.kwargs.get('pk')})


#                                                                                                                 DETAIL
# TICKET DETAIL VIEW
class TicketDetailView(LoginRequiredMixin, DetailView):
    model = Ticket
    context_object_name = 'ticket'
    template_name = 'help_desk/help_desk/detail/ticket/ticket_detail.html'

    def get_queryset(self):
        return self.model.objects.select_related('detail').all()



#                                                                                                                   LIST
# TICKET LIST VIEW
class TicketsListView(LoginRequiredMixin, ListView):
    model = Ticket
    template_name = 'help_desk/help_desk/list/tickets/tickets_list.html'
    context_object_name = 'tickets'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["latest_articles"] = articles_latest()
        context["closest_birthdays"] = employees_closest_birthdays()
        context["newest_employees"] = employees_newest()
        return context

    def get_queryset(self):
        self.pattern = self.kwargs.get('pattern')

        if self.pattern == 'my/open':
            return self.model.objects.select_related('detail').filter(detail__status=0,
                                                                      detail__created_by=self.request.user)

        elif self.pattern == 'my/processing':
            return self.model.objects.select_related('detail').filter(~Q(detail__status__in=[0, 4]),
                                                                      detail__created_by=self.request.user)

        elif self.pattern == 'my/closed':
            return self.model.objects.select_related('detail').filter(detail__status=4,
                                                                      detail__created_by=self.request.user)

        elif self.pattern == 'to/me/assigned':
            return self.model.objects.select_related('detail').filter(detail__status=1,
                                                                      detail__assignee=self.request.user)
        elif self.pattern == 'by/me/assigned':
            return self.model.objects.select_related('detail').filter(detail__status=1,
                                                                      detail__processed_by=self.request.user)

        elif self.pattern == 'by/me/accepted':
            return self.model.objects.select_related('detail').filter(detail__status=2,
                                                                      detail__processed_by=self.request.user)

        elif self.pattern == 'by/me/discarded':
            return self.model.objects.select_related('detail').filter(detail__status=3,
                                                                      detail__processed_by=self.request.user)

        elif self.pattern == 'by/me/closed':
            return self.model.objects.select_related('detail').filter(detail__status=4,
                                                                      detail__processed_by=self.request.user)
        elif self.pattern == 'all/open':
            return self.model.objects.select_related('detail').filter(~Q(detail__created_by=self.request.user),
                                                                      detail__status=0)

        elif self.pattern == 'all/accepted':
            return self.model.objects.select_related('detail').filter(detail__status=2)

        elif self.pattern == 'all/assigned':
            return self.model.objects.select_related('detail').filter(detail__status=1)

        elif self.pattern == 'all/discarded':
            return self.model.objects.select_related('detail').filter(detail__status=3)

        elif self.pattern == 'all/closed':
            return self.model.objects.select_related('detail').filter(detail__status=4)


#                                                                                                                METHODS
# TICKET DETAIL CLOSE METHOD
def ticket_close_method(request, pk):
    ticket_detail = get_object_or_404(TicketDetail, pk=pk)
    ticket_detail.status = 4
    ticket_detail.save()

    return HttpResponseRedirect(reverse_lazy('helpdesk:tickets_list', kwargs={'pattern': 'my/closed'}))


# TICKET DETAIL CLOSE METHOD
def ticket_open_method(request, pk):
    ticket_detail = get_object_or_404(TicketDetail, pk=pk)
    ticket_detail.status = 0
    ticket_detail.save()

    return HttpResponseRedirect(reverse_lazy('helpdesk:tickets_list', kwargs={'pattern': 'my/open'}))

