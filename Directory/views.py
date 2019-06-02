from django.views.generic import TemplateView, ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from HumanResources.models import Profile
from News.functions import articles_latest, employees_newest, employees_closest_birthdays


class ContactsListView(LoginRequiredMixin, ListView):
    model = Profile
    context_object_name = 'contacts'
    template_name = 'directory/list/contacts/contacts_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["latest_articles"] = articles_latest()
        context["closest_birthdays"] = employees_closest_birthdays()
        context["newest_employees"] = employees_newest()
        return context

