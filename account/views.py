from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Create your views here.
from .forms import UserRegistrationForM


@login_required
def dashboard(request):
    return render(request,
    'account/dashboard.html',
    {'section':'dashboard'}
    )

def register(request):
    if request.method == 'POST':
        user_form = UserRegistrationForM(request.POST)
        if user_form.is_valid():
            new_user = user_form.save(commit=False)
            new_user.set_password(user_form.clean_data['password'])
            new_user.save()
            return render(request, 'account/register_done.html',
            {'new_user':new_user})
