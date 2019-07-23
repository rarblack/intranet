from django.views.generic import TemplateView


# HOME TEMPLATE VIEW
class HomeTemplateView(TemplateView):
    template_name = 'home/home_template.html'
