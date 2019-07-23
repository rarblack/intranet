from django.db.models import Q
from django.http import HttpResponseRedirect
from django.views.generic import CreateView, UpdateView, DeleteView, TemplateView, ListView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy
from django.utils import timezone

from .models import Ticket, TicketDetail, Activity, Message, Car
from News.functions import articles_latest, employees_newest, employees_closest_birthdays


#                                                                                                                 CREATE
# TICKET CREATE VIEW
class TicketCreateView(LoginRequiredMixin, CreateView):
    model = Ticket
    fields = ['car', 'trip', 'origin', 'destination', 'leave_time', 'return_time', 'duration', 'importance', 'note']
    template_name = 'transportation/create/ticket/ticket_create.html'
    success_url = reverse_lazy('transportation:tickets_list', kwargs={'pattern': 'my/open'})

    def form_valid(self, form):
        detail = TicketDetail.objects.create(status=0,
                                             created_by=self.request.user)
        Activity.objects.create(detail=detail,
                                status=detail.status,
                                assignee=detail.assignee,
                                created_by=detail.created_by,
                                created_at=detail.created_at)
        self.object = form.save(commit=False)
        self.object.detail = detail
        self.object.save()
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["latest_articles"] = articles_latest()
        context["closest_birthdays"] = employees_closest_birthdays()
        context["newest_employees"] = employees_newest()
        return context


# CAR CREATE VIEW
class CarCreateView(LoginRequiredMixin, CreateView):
    model = Car
    fields = ['brand', 'model', 'type']
    template_name = 'transportation/create/car/car_create.html'
    success_url = reverse_lazy('transportation:cars_list')

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.created_by = self.request.user
        self.object.created_at = timezone.now()
        self.object.save()
        return super(CarCreateView, self).form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["latest_articles"] = articles_latest()
        context["closest_birthdays"] = employees_closest_birthdays()
        context["newest_employees"] = employees_newest()
        return context


# MESSAGE CREATE VIEW
class MessageCreateView(LoginRequiredMixin, CreateView):

    model = Message
    fields = ['reason', 'explanation']
    template_name = 'help_desk/help_desk/create/message/message_create.html'
    success_url = reverse_lazy('helpdesk:navigation_template', kwargs={'pattern': 'main'})

    def dispatch(self, request, *args, **kwargs):

        # Custom Variables
        self.ticket = Ticket.objects.filter(created_by=request.user).latest('created_at')

        # Default Dispatch Mechanism
        if request.method.lower() in self.http_method_names:
            handler = getattr(self, request.method.lower(), self.http_method_not_allowed)
        else:
            handler = self.http_method_not_allowed
        return handler(request, *args, **kwargs)

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.save()
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["latest_articles"] = articles_latest()
        context["closest_birthdays"] = employees_closest_birthdays()
        context["newest_employees"] = employees_newest()
        return context


#                                                                                                                 UPDATE
# TICKET UPDATE VIEW
class TicketUpdateView(LoginRequiredMixin, UpdateView):
    model = Ticket
    fields = ['car', 'trip', 'origin', 'destination', 'leave_time', 'return_time', 'duration', 'importance', 'note']
    template_name = 'transportation/update/ticket/ticket_update.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["latest_articles"] = articles_latest()
        context["closest_birthdays"] = employees_closest_birthdays()
        context["newest_employees"] = employees_newest()
        return context

    def get_success_url(self):
        return reverse_lazy('transportation:ticket_detail', kwargs={'pk': self.kwargs.get('pk')})


# TICKET DETAIL UPDATE VIEW
class TicketDetailUpdateView(LoginRequiredMixin, UpdateView):
    model = TicketDetail
    fields = ['status', 'assignee']
    template_name = 'transportation/update/ticket_detail/ticket_detail_update.html'

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

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["latest_articles"] = articles_latest()
        context["closest_birthdays"] = employees_closest_birthdays()
        context["newest_employees"] = employees_newest()
        return context

    def get_success_url(self):
        return reverse_lazy('transportation:ticket_detail', kwargs={'pk': self.kwargs.get('pk')})


# CAR UPDATE VIEW
class CarUpdateView(LoginRequiredMixin, UpdateView):
    model = Car
    fields = ['brand', 'model', 'type']
    template_name = 'transportation/update/car/car_update.html'
    context_object_name = 'car'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["latest_articles"] = articles_latest()
        context["closest_birthdays"] = employees_closest_birthdays()
        context["newest_employees"] = employees_newest()
        return context


#                                                                                                                 DETAIL
# TICKET DETAIL VIEW
class TicketDetailView(LoginRequiredMixin, DetailView):
    model = Ticket
    context_object_name = 'ticket'
    template_name = 'transportation/detail/ticket/ticket_detail.html'

    def get_queryset(self):
        return self.model.objects.select_related('detail').all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['activities'] = Activity.objects.filter(detail_id=self.kwargs.get('pk'))
        context["latest_articles"] = articles_latest()
        context["closest_birthdays"] = employees_closest_birthdays()
        context["newest_employees"] = employees_newest()
        return context


# CAR DETAIL VIEW
class CarDetailView(LoginRequiredMixin, DetailView):
    model = Car
    template_name = 'transportation/detail/car/car_detail.html'
    context_object_name = 'car'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["latest_articles"] = articles_latest()
        context["closest_birthdays"] = employees_closest_birthdays()
        context["newest_employees"] = employees_newest()
        return context


#                                                                                                                   LIST
# TICKET LIST VIEW
class TicketsListView(LoginRequiredMixin, ListView):
    model = Ticket
    template_name = 'transportation/list/tickets/tickets_list.html'
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


# CARS LIST VIEW
class CarsListView(LoginRequiredMixin, ListView):
    model = Car
    template_name = 'transportation/list/cars/cars_list.html'
    context_object_name = 'cars'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["latest_articles"] = articles_latest()
        context["closest_birthdays"] = employees_closest_birthdays()
        context["newest_employees"] = employees_newest()
        return context


#                                                                                                                METHODS
# TICKET DETAIL CLOSE METHOD
def ticket_close_method(request, pk):
    ticket_detail = get_object_or_404(TicketDetail, pk=pk)
    ticket_detail.status = 4
    ticket_detail.save()

    return HttpResponseRedirect(reverse_lazy('transportation:tickets_list', kwargs={'pattern': 'my/closed'}))


# TICKET DETAIL CLOSE METHOD
def ticket_open_method(request, pk):
    ticket_detail = get_object_or_404(TicketDetail, pk=pk)
    ticket_detail.status = 0
    ticket_detail.save()

    return HttpResponseRedirect(reverse_lazy('transportation:tickets_list', kwargs={'pattern': 'my/open'}))

