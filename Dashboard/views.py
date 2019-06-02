from django.views import generic

from News.functions import articles_latest, employees_closest_birthdays, employees_newest


class DashboardTemplateView(generic.TemplateView):
    template_name = 'dashboard/template/dashboard_template.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["latest_articles"] = articles_latest()
        context["closest_birthdays"] = employees_closest_birthdays()
        context["newest_employees"] = employees_newest()
        return context
