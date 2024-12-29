from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.views import LoginView
from django.urls import reverse
from .forms import CustomRegistrationForm
from apps.clients.models import Client
from .backends import CustomAuthBackend
from apps.providers.models import Provider  # Add this import

def register_view(request):
    if request.method == 'POST':
        form = CustomRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = CustomRegistrationForm()
    return render(request, 'registration/register.html', {'form': form})

class CustomLoginView(LoginView):
    template_name = 'registration/login.html'

    def form_valid(self, form):
        response = super().form_valid(form)
        user = form.get_user()
        
        if Provider.objects.filter(user=user).exists():
            return redirect('providers:provider_dashboard')  # Updated with namespace
        return redirect('clients_dashboard')
@login_required
def dashboard_view(request):
    if hasattr(request.user, 'provider'):
        return redirect('providers_dashboard')
    elif hasattr(request.user, 'client'):
        return redirect('clients_dashboard')
    return redirect('home')

def login_view(request):
    if request.method == 'POST':
        # Your authentication logic here
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            backend = CustomAuthBackend()
            return redirect(backend.get_user_redirect_url(user))
    return render(request, 'login.html')