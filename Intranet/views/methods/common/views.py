from django.http import HttpResponseRedirect
from django.urls import reverse


def render_home_or_welcome(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse('welcome'))
    return HttpResponseRedirect(reverse('home'))
