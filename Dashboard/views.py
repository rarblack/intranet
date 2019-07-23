from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin


class DashboardTemplateView(LoginRequiredMixin, generic.TemplateView):
    template_name = 'dashboard/template/dashboard_template.html'
