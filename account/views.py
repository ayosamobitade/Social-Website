from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Create your views here.

from django.http import HttpResponse
from django.contrib.auth import authenticate, login


@login_required
def dashboard(request):
    return render(request,
    'account/dashboear.html',
    {'section':'dashboard'}
    )
