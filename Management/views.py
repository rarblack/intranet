from django.shortcuts import render_to_response
from django.views import generic


class TestsView(generic.TemplateView):
    template_name = 'test.html'