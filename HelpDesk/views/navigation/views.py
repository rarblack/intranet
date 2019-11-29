from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin


#                                                                                                               TEMPLATE
class NavigationTemplateView(LoginRequiredMixin, TemplateView):
    template_name = 'help_desk/navigation/template/navigation_template.html'
