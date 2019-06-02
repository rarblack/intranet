from django.shortcuts import render
from django.contrib.auth.decorators import login_required, permission_required
from django.http import HttpResponse


@login_required
def hr(request):

    context = {
    }
    return HttpResponse('HR app')