from django.views.generic import CreateView, TemplateView, ListView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy

from GuestControl.models.external.entrance_card.models import ExternalEntranceCardModel
from .functions import base64_to_content_file


#                                                                                                                 CREATE
class ExternalEntranceCardCreateView(LoginRequiredMixin, CreateView):
    model = ExternalEntranceCardModel
    fields = ['name', 'surname', 'company', 'enter_datetime', 'leave_datetime']
    template_name = 'guest_control/external/entrance_card/create/card_create.html'
    success_url = reverse_lazy('guest_control:entrance_cards_list')

    def form_valid(self, form):
        username = self.request.POST['name'] + self.request.POST['surname']
        datetime = self.request.POST['leave_datetime']
        data, name = base64_to_content_file.convert(
            self.request.POST['base64'],
            username,
            datetime
        )

        self.object = form.save(commit=False)
        self.object.image = data
        self.object.creator = self.request.user
        self.object.save()

        return super().form_valid(form)


#                                                                                                                 UPDATE


#                                                                                                                 DETAIL
class ExternalEntranceCardDetailView(DetailView):
    model = ExternalEntranceCardModel
    context_object_name = 'card'
    template_name = 'guest_control/external/entrance_card/detail/card_detail.html'

    def get_queryset(self):
        return self.model.objects.all()


#                                                                                                               TEMPLATE
class ExternalEntranceCardTemplateView(LoginRequiredMixin, TemplateView):
    template_name = 'guest_control/external/entrance_card/template/card_template.html'


#                                                                                                                   LIST
class ExternalEntranceCardsListView(LoginRequiredMixin, ListView):
    model = ExternalEntranceCardModel
    template_name = 'guest_control/external/entrance_card/list/card_list.html'
    context_object_name = 'cards'

    def get_queryset(self):
        return self.model.objects.all().order_by('-creation_datetime')

