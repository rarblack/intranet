from django.db.models import Q
from django.http import HttpResponseRedirect
from django.views.generic import CreateView, UpdateView, DeleteView, TemplateView, ListView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy
from django.utils import timezone

from .models import ExternalVisitTicket, ExternalVisitTicketDetail, InternalVisitTicket, InternalVisitTicketDetail, VisitorEntranceCardModel
from News.functions import articles_latest, employees_closest_birthdays, employees_newest
from . import functions


#                                                                                                                 CREATE
# EXTERNAL VISIT TICKET CREATE VIEW
class ExternalVisitTicketCreateView(LoginRequiredMixin, CreateView):
    model = ExternalVisitTicket
    fields = ['name', 'surname', 'company', 'subject', 'purpose', 'contact_type', 'contact', 'email', 'host', 'visit_datetime', 'leave_datetime', 'importance', 'note']
    template_name = 'guestcontrol/create/external_visit_ticket/external_visit_ticket_create.html'
    success_url = reverse_lazy('guestcontrol:external_visit_tickets_list', kwargs={'pattern': 'my/open'})

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["latest_articles"] = articles_latest()
        context["closest_birthdays"] = employees_closest_birthdays()
        context["newest_employees"] = employees_newest()
        return context

    def form_valid(self, form):
        detail = ExternalVisitTicketDetail.objects.create(status=0,
                                                          created_by=self.request.user,
                                                          created_at=timezone.now())
        self.object = form.save(commit=False)
        self.object.detail = detail
        self.object.save()
        return super().form_valid(form)


# INTERNAL VISIT TICKET CREATE VIEW
class InternalVisitTicketCreateView(LoginRequiredMixin, CreateView):
    model = InternalVisitTicket
    fields = ['user', 'subject', 'purpose', 'host', 'visit_datetime', 'leave_datetime', 'importance', 'note']
    template_name = 'guestcontrol/create/internal_visit_ticket/internal_visit_ticket_create.html'
    success_url = reverse_lazy('guestcontrol:internal_visit_tickets_list', kwargs={'pattern': 'my/open'})

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["latest_articles"] = articles_latest()
        context["closest_birthdays"] = employees_closest_birthdays()
        context["newest_employees"] = employees_newest()
        return context

    def form_valid(self, form):
        detail = InternalVisitTicketDetail.objects.create(status=0,
                                                          created_by=self.request.user,
                                                          created_at=timezone.now())
        self.object = form.save(commit=False)
        self.object.detail = detail
        self.object.save()
        return super().form_valid(form)


# VISITOR ENTRANCE CARD CREATE VIEW
class VisitorEntranceCardCreateView(CreateView):
    model = VisitorEntranceCardModel
    fields = ['name', 'surname', 'company', 'enter_datetime', 'leave_datetime']
    template_name = 'guestcontrol/create/visitor_entrance_card/visitor_entrance_card_create.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["latest_articles"] = articles_latest()
        context["closest_birthdays"] = employees_closest_birthdays()
        context["newest_employees"] = employees_newest()
        return context

    def form_valid(self, form):
        self.username = self.request.POST['name'] + self.request.POST['surname']
        self.datetime = self.request.POST['leave_datetime']
        self.data, self.name = functions.base64_to_content_file(self.request.POST['base64'], self.username, self.datetime)

        self.object = form.save(commit=False)
        self.object.image = self.data
        self.object.creator = self.request.user
        self.object.save()

        return super(VisitorEntranceCardCreateView, self).form_valid(form)

    def get_success_url(self):
        return reverse_lazy('guestcontrol:visitor_entrance_card_detail', kwargs={'pk': self.object.pk})


#                                                                                                                 UPDATE
# EXTERNAL VISIT TICKET UPDATE VIEW
class ExternalVisitTicketUpdateView(LoginRequiredMixin, UpdateView):
    model = ExternalVisitTicket
    fields = ['name', 'surname', 'company', 'subject', 'purpose', 'contact_type', 'contact', 'email', 'host', 'visit_datetime', 'leave_datetime', 'importance', 'note']
    template_name = 'guestcontrol/update/external_visit_ticket/external_visit_ticket_update.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["latest_articles"] = articles_latest()
        context["closest_birthdays"] = employees_closest_birthdays()
        context["newest_employees"] = employees_newest()
        return context

    def get_success_url(self):
        return reverse_lazy('guestcontrol:external_visit_ticket_detail', kwargs={'pk': self.kwargs.get('pk')})


# TICKET DETAIL UPDATE VIEW
# class ExternalVisitTicketDetailUpdateView(LoginRequiredMixin, UpdateView):
#     model = ExternalVisitTicketDetail
#     fields = ['status', 'arrive_time_actual', 'leave_time_actual']
#     template_name = 'guestcontrol/update/external_visit_ticket_detail/ticket_detail_update.html'
#
#     def form_valid(self, form):
#         self.object = form.save(commit=False)
#         self.object.processed_by = self.request.user
#         self.object.processed_at = timezone.now()
#         self.object.save()
#         return super().form_valid(form)
#
#     def get_success_url(self):
#         return reverse_lazy('guestcontrol:ticket_detail', kwargs={'pk': self.kwargs.get('pk')})
#

# INTERNAL VISIT TICKET UPDATE VIEW
class InternalVisitTicketUpdateView(LoginRequiredMixin, UpdateView):
    model = InternalVisitTicket
    fields = ['user', 'subject', 'purpose', 'host', 'visit_datetime', 'leave_datetime', 'importance', 'note']
    template_name = 'guestcontrol/update/internal_visit_ticket/internal_visit_ticket_update.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["latest_articles"] = articles_latest()
        context["closest_birthdays"] = employees_closest_birthdays()
        context["newest_employees"] = employees_newest()
        return context

    def get_success_url(self):
        return reverse_lazy('guestcontrol:internal_visit_ticket_detail', kwargs={'pk': self.kwargs.get('pk')})


# INTERNAL VISIT TICKET DETAIL UPDATE VIEW
# class InternalVisitTicketDetailUpdateView(LoginRequiredMixin, UpdateView):
#     model = InternalVisitTicketDetail
#     fields = ['status', 'arrive_time_actual', 'leave_time_actual']
#     template_name = 'guestcontrol/update/internal_visit_ticket_detail/internal_visit_ticket_detail_update.html'
#
#     def form_valid(self, form):
#         self.object = form.save(commit=False)
#         self.object.processed_by = self.request.user
#         self.object.processed_at = timezone.now()
#         self.object.save()
#         return super().form_valid(form)
#
#     def get_success_url(self):
#         return reverse_lazy('guestcontrol:internal_visit_ticket_detail', kwargs={'pk': self.kwargs.get('pk')})


#                                                                                                                 DETAIL
# EXTERNAL VISIT TICKET DETAIL VIEW
class ExternalVisitTicketDetailView(LoginRequiredMixin, DetailView):
    model = ExternalVisitTicket
    context_object_name = 'ticket'
    template_name = 'guestcontrol/detail/external_visit_ticket/external_visit_ticket_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["latest_articles"] = articles_latest()
        context["closest_birthdays"] = employees_closest_birthdays()
        context["newest_employees"] = employees_newest()
        return context

    def get_queryset(self):
        return self.model.objects.select_related('detail').all()


# INTERNAL VISIT TICKET DETAIL VIEW
class InternalVisitTicketDetailView(LoginRequiredMixin, DetailView):
    model = InternalVisitTicket
    context_object_name = 'ticket'
    template_name = 'guestcontrol/detail/internal_visit_ticket/internal_visit_ticket_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["latest_articles"] = articles_latest()
        context["closest_birthdays"] = employees_closest_birthdays()
        context["newest_employees"] = employees_newest()
        return context

    def get_queryset(self):
        return self.model.objects.select_related('detail').all()


# VISITOR ENTRANCE CARD DETAIL VIEW
class VisitorEntranceCardDetailView(DetailView):
    model = VisitorEntranceCardModel
    context_object_name = 'card'
    template_name = 'guestcontrol/detail/visitor_entrance_card/visitor_entrance_card_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["latest_articles"] = articles_latest()
        context["closest_birthdays"] = employees_closest_birthdays()
        context["newest_employees"] = employees_newest()
        return context

    def get_queryset(self):
        return self.model.objects.all()


#                                                                                                               TEMPLATE
# VISITOR ENTRANCE CARD TEMPLATE VIEW
class VisitorEntranceCardTemplateView(TemplateView):
    template_name = 'guestcontrol/template/visitor_entrance_card/visitor_entrance_card_template.html'

    def get_context_data(self, **kwargs):
        context = super(VisitorEntranceCardTemplateView, self).get_context_data(**kwargs)
        card = get_object_or_404(VisitorEntranceCardModel, pk=self.kwargs.get('pk'))
        context['card'] = card
        context["latest_articles"] = articles_latest()
        context["closest_birthdays"] = employees_closest_birthdays()
        context["newest_employees"] = employees_newest()
        return context


#                                                                                                                   LIST
# EXTERNAL VISIT TICKET LIST VIEW
class ExternalVisitTicketsListView(LoginRequiredMixin, ListView):
    model = ExternalVisitTicket
    template_name = 'guestcontrol/list/external_visit_tickets/external_visit_tickets_list.html'
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
                                                                      detail__created_by=self.request.user).order_by('visit_datetime')

        # elif self.pattern == 'my/processing':
        #     return self.model.objects.select_related('detail').filter(~Q(detail__status__in=[0, 4]),
        #                                                               detail__created_by=self.request.user)

        elif self.pattern == 'my/closed':
            return self.model.objects.select_related('detail').filter(detail__status=4,
                                                                      detail__created_by=self.request.user).order_by('-visit_datetime')
        #
        # elif self.pattern == 'to/me/assigned':
        #     return self.model.objects.select_related('detail').filter(detail__status=1,
        #                                                               detail__assignee=self.request.user)
        # elif self.pattern == 'by/me/assigned':
        #     return self.model.objects.select_related('detail').filter(detail__status=1,
        #                                                               detail__processed_by=self.request.user)
        #
        # elif self.pattern == 'by/me/accepted':
        #     return self.model.objects.select_related('detail').filter(detail__status=2,
        #                                                               detail__processed_by=self.request.user)
        #
        # elif self.pattern == 'by/me/discarded':
        #     return self.model.objects.select_related('detail').filter(detail__status=3,
        #                                                               detail__processed_by=self.request.user)

        # elif self.pattern == 'by/me/closed':
        #     return self.model.objects.select_related('detail').filter(detail__status=4,
        #                                                               detail__processed_by=self.request.user)

        elif self.pattern == 'all/open':
            return self.model.objects.select_related('detail').filter(~Q(detail__created_by=self.request.user),
                                                                      detail__status=0).order_by('visit_datetime')

        # elif self.pattern == 'all/accepted':
        #     return self.model.objects.select_related('detail').filter(detail__status=2)
        #
        # elif self.pattern == 'all/assigned':
        #     return self.model.objects.select_related('detail').filter(detail__status=1)
        #
        # elif self.pattern == 'all/discarded':
        #     return self.model.objects.select_related('detail').filter(detail__status=3)

        elif self.pattern == 'all/closed':
            return self.model.objects.select_related('detail').filter(detail__status=4).order_by('-visit_datetime')


# INTERNAL VISIT TICKETS LIST VIEW
class InternalVisitTicketsListView(LoginRequiredMixin, ListView):
    model = InternalVisitTicket
    template_name = 'guestcontrol/list/internal_visit_tickets/internal_visit_tickets_list.html'
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
                                                                      detail__created_by=self.request.user).order_by(
                'visit_datetime')

        # elif self.pattern == 'my/processing':
        #     return self.model.objects.select_related('detail').filter(~Q(detail__status__in=[0, 4]),
        #                                                               detail__created_by=self.request.user)

        elif self.pattern == 'my/closed':
            return self.model.objects.select_related('detail').filter(detail__status=4,
                                                                      detail__created_by=self.request.user).order_by(
                '-visit_datetime')
        #
        # elif self.pattern == 'to/me/assigned':
        #     return self.model.objects.select_related('detail').filter(detail__status=1,
        #                                                               detail__assignee=self.request.user)
        # elif self.pattern == 'by/me/assigned':
        #     return self.model.objects.select_related('detail').filter(detail__status=1,
        #                                                               detail__processed_by=self.request.user)
        #
        # elif self.pattern == 'by/me/accepted':
        #     return self.model.objects.select_related('detail').filter(detail__status=2,
        #                                                               detail__processed_by=self.request.user)
        #
        # elif self.pattern == 'by/me/discarded':
        #     return self.model.objects.select_related('detail').filter(detail__status=3,
        #                                                               detail__processed_by=self.request.user)

        # elif self.pattern == 'by/me/closed':
        #     return self.model.objects.select_related('detail').filter(detail__status=4,
        #                                                               detail__processed_by=self.request.user)

        elif self.pattern == 'all/open':
            return self.model.objects.select_related('detail').filter(~Q(detail__created_by=self.request.user),
                                                                      detail__status=0).order_by('visit_datetime')

        # elif self.pattern == 'all/accepted':
        #     return self.model.objects.select_related('detail').filter(detail__status=2)
        #
        # elif self.pattern == 'all/assigned':
        #     return self.model.objects.select_related('detail').filter(detail__status=1)
        #
        # elif self.pattern == 'all/discarded':
        #     return self.model.objects.select_related('detail').filter(detail__status=3)

        elif self.pattern == 'all/closed':
            return self.model.objects.select_related('detail').filter(detail__status=4).order_by('-visit_datetime')


# VISITOR ENTRANCE CARDS LIST VIEW
class VisitorEntranceCardsListView(ListView):
    model = VisitorEntranceCardModel
    template_name = 'guestcontrol/list/visitor_entrance_card/visitor_entrance_card_list.html'
    context_object_name = 'cards'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["latest_articles"] = articles_latest()
        context["closest_birthdays"] = employees_closest_birthdays()
        context["newest_employees"] = employees_newest()
        return context

    def get_queryset(self):
        return self.model.objects.all().order_by('-creation_datetime')


#                                                                                                                METHODS
# EXTERNAL VISIT TICKET DETAIL CLOSE METHOD
def external_visit_ticket_close_method(request, pk):
    ticket_detail = get_object_or_404(ExternalVisitTicketDetail, pk=pk)
    ticket_detail.status = 4
    ticket_detail.save()

    return HttpResponseRedirect(reverse_lazy('guestcontrol:external_visit_tickets_list', kwargs={'pattern': 'my/closed'})+'#content')


# EXTERNAL VISIT TICKET DETAIL CLOSE METHOD
def external_visit_ticket_open_method(request, pk):
    ticket_detail = get_object_or_404(ExternalVisitTicketDetail, pk=pk)
    ticket_detail.status = 0
    ticket_detail.save()

    return HttpResponseRedirect(reverse_lazy('guestcontrol:external_visit_tickets_list', kwargs={'pattern': 'my/open'})+'#content')


# INTERNAL VISIT TICKET DETAIL CLOSE METHOD
def internal_visit_ticket_close_method(request, pk):
    ticket_detail = get_object_or_404(InternalVisitTicketDetail, pk=pk)
    ticket_detail.status = 4
    ticket_detail.save()

    return HttpResponseRedirect(reverse_lazy('guestcontrol:internal_visit_tickets_list', kwargs={'pattern': 'my/closed'})+'#content')


# INTERNAL VISIT TICKET DETAIL CLOSE METHOD
def internal_visit_ticket_open_method(request, pk):
    ticket_detail = get_object_or_404(InternalVisitTicketDetail, pk=pk)
    ticket_detail.status = 0
    ticket_detail.save()

    return HttpResponseRedirect(reverse_lazy('guestcontrol:internal_visit_tickets_list', kwargs={'pattern': 'my/open'})+'#content')