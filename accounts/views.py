from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from apps.clients.models import Client
from apps.providers.models import Provider

def register_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'registration/register.html', {'form': form})

def login_success(request):
    if request.user.is_authenticated:
        if Client.objects.filter(user=request.user).exists():
            return redirect('client_dashboard')
        elif Provider.objects.filter(user=request.user).exists():
            return redirect('provider_dashboard')
   
         