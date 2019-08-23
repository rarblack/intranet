from django.db.models import Q
from django.http import HttpResponseRedirect
from django.views.generic import CreateView, UpdateView, ListView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy
from django.utils import timezone

from GuestControl.models.internal.visitor.models import InternalVisitorTicketModel, InternalVisitorTicketDetailModel


#                                                                                                                 CREATE
class TicketCreateView(LoginRequiredMixin, CreateView):
    model = InternalVisitorTicketModel
    fields = ['user', 'subject', 'purpose', 'host', 'visit_datetime', 'leave_datetime', 'importance', 'note']
    template_name = 'guest_control/internal/visitor/create/ticket_create.html'
    success_url = reverse_lazy('guest_control:internal_visitor_tickets_list', kwargs={'pattern': 'my/open'})

    def form_valid(self, form):
        detail = InternalVisitorTicketDetailModel.objects.create(
            status=0,
            created_by=self.request.user,
            created_at=timezone.now()
        )

        self.object = form.save(commit=False)
        self.object.detail = detail
        self.object.save()
        return super().form_valid(form)


#                                                                                                                 UPDATE
class TicketUpdateView(LoginRequiredMixin, UpdateView):
    model = InternalVisitorTicketModel
    fields = ['user', 'subject', 'purpose', 'host', 'visit_datetime', 'leave_datetime', 'importance', 'note']
    template_name = 'guest_control/internal/visitor/update/ticket_update.html'

    def get_success_url(self):
        return reverse_lazy('guest_control:internal_visitor_ticket_detail', kwargs={'pk': self.kwargs.get('pk')})


#                                                                                                                 DETAIL
class TicketDetailView(LoginRequiredMixin, DetailView):
    model = InternalVisitorTicketModel
    context_object_name = 'ticket'
    template_name = 'guest_control/internal/visitor/detail/ticket_detail.html'

    def get_queryset(self):
        return self.model.objects.select_related('detail').all()


#                                                                                                                   LIST
# INTERNAL VISITOR TICKETS LIST VIEW
class TicketsListView(LoginRequiredMixin, ListView):
    model = InternalVisitorTicketModel
    template_name = 'guest_control/internal/visitor/list/ticket_list.html'
    context_object_name = 'tickets'

    def get_queryset(self):
        self.pattern = self.kwargs.get('pattern')

        if self.pattern == 'my/open':
            return self.model.objects. \
                select_related('detail'). \
                filter(detail__status=0, detail__created_by=self.request.user). \
                order_by('visit_datetime')

        # elif self.pattern == 'my/processing':
        #     return self.model.objects.select_related('detail').filter(~Q(detail__status__in=[0, 4]),
        #                                                               detail__created_by=self.request.user)

        elif self.pattern == 'my/closed':
            return self.model.objects. \
                select_related('detail'). \
                filter(detail__status=4, detail__created_by=self.request.user). \
                order_by('-visit_datetime')
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
            return self.model.objects. \
                select_related('detail'). \
                filter(~Q(detail__created_by=self.request.user), detail__status=0). \
                order_by('visit_datetime')

        # elif self.pattern == 'all/accepted':
        #     return self.model.objects.select_related('detail').filter(detail__status=2)
        #
        # elif self.pattern == 'all/assigned':
        #     return self.model.objects.select_related('detail').filter(detail__status=1)
        #
        # elif self.pattern == 'all/discarded':
        #     return self.model.objects.select_related('detail').filter(detail__status=3)

        elif self.pattern == 'all/closed':
            return self.model.objects. \
                select_related('detail'). \
                filter(detail__status=4). \
                order_by('-visit_datetime')


#                                                                                                                METHODS
def ticket_close_method(request, pk):
    ticket_detail = get_object_or_404(
        InternalVisitorTicketDetailModel, pk=pk
    )
    ticket_detail.status = 4
    ticket_detail.save()

    return HttpResponseRedirect(
        reverse_lazy('guest_control:internal_visitor_tickets_list', kwargs={'pattern': 'my/closed'})
        + '#content'
    )


def ticket_open_method(request, pk):
    ticket_detail = get_object_or_404(
        InternalVisitorTicketDetailModel, pk=pk
    )
    ticket_detail.status = 0
    ticket_detail.save()

    return HttpResponseRedirect(
        reverse_lazy('guest_control:internal_visitor_tickets_list', kwargs={'pattern': 'my/open'})
        + '#content'
    )


#                                                                                                                 CREATE
#                                                                                                                 UPDATE
#                                                                                                                 DETAIL
#                                                                                                                   LIST
#                                                                                                                METHODS
#                                                                                                                METHODS
