from django.shortcuts import render, reverse, get_object_or_404
from .forms import PasswordChangeForm
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
# Create your views here.


def change_password(request):
    user = get_object_or_404(User,
                                 pk=request.user.pk)
    if request.method == 'POST':
        form = PasswordChangeForm(request.POST)
        if form.is_valid():
            if form.cleaned_data['password1'] == form.cleaned_data['password2']:
                user.set_password(form.cleaned_data['password1'])
                user.save()
                return HttpResponseRedirect(reverse('dashboard'))
    else:
        form = PasswordChangeForm()
    return render(request,
                  'settings/change-password.html',
                  {'form': form})
