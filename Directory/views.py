from django.views.generic import TemplateView, ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from HumanResources.models import Profile


class ContactsListView(LoginRequiredMixin, ListView):
    model = Profile
    context_object_name = 'contacts'
    template_name = 'directory/list/contacts/contacts_list.html'
