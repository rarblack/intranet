from django.views.generic import TemplateView, ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from User.models import Profile


class ContactsListView(LoginRequiredMixin, ListView):
    model = Profile
    context_object_name = 'contacts'
    template_name = 'directory/default/list/contacts_list.html'
