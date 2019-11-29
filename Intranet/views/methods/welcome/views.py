from django.shortcuts import render, reverse
from django.http import HttpResponseRedirect


def render_welcome(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect(reverse('home'))
    return render(
        request,
        'singles/welcome/template/template_welcome.html',
        context={'WELCOME': True})
