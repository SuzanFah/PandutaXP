from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.views import LoginView
from django.urls import reverse
from .forms import CustomRegistrationForm
from apps.clients.models import Client
from .backends import CustomAuthBackend
from apps.providers.models import Provider
from apps.clients.forms import ClientSignUpForm
from apps.providers.forms import ProviderSignUpForm

def register_view(request):
    if request.method == 'POST':
        user_type = request.POST.get('user_type', 'CLIENT')
        form = ProviderSignUpForm(request.POST) if user_type == 'PROVIDER' else ClientSignUpForm(request.POST)
        
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('providers_dashboard' if user_type == 'PROVIDER' else 'clients_dashboard')
    else:
        form = CustomRegistrationForm()
    return render(request, 'registration/register.html', {'form': form})

class CustomLoginView(LoginView):
    template_name = 'registration/login.html'

    def form_valid(self, form):
        response = super().form_valid(form)
        user = form.get_user()
        if hasattr(user, 'provider'):
            return redirect('providers_dashboard')
        elif hasattr(user, 'client'):
            return redirect('clients_dashboard')
        return response

@login_required
def dashboard_view(request):
    if hasattr(request.user, 'provider'):
        return redirect('providers_dashboard')
    elif hasattr(request.user, 'client'):
        return redirect('clients_dashboard')
    return redirect('home')

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect('providers_dashboard' if hasattr(user, 'provider') else 'clients_dashboard')
    return render(request, 'registration/login.html')