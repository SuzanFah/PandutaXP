from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from .forms import ProviderSignUpForm, ServiceForm  # Add ServiceForm here
from .models import Service, Provider

def provider_signup(request):
    if request.method == 'POST':
        form = ProviderSignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            Provider.objects.create(
                user=user,
                phone=form.cleaned_data.get('phone'),
                address=form.cleaned_data.get('address'),
                service_type=form.cleaned_data.get('service_type')
            )
            return redirect('providers:provider_login')
    else:
        form = ProviderSignUpForm()
    return render(request, 'providers/signup.html', {'form': form})

@login_required
def provider_dashboard(request):
    if not hasattr(request.user, 'provider'):
        return redirect('home')
    return render(request, 'providers/dashboard.html', {'user': request.user})

def provider_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None and Provider.objects.filter(user=user).exists():
            login(request, user)
            return redirect('providers:provider_dashboard')
    return render(request, 'providers/login.html')

@login_required
def update_status(request):
    return render(request, 'providers/update_status.html')

from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Service

@login_required
def manage_services(request):
    services = Service.objects.filter(provider=request.user.provider)
    return render(request, 'providers/services.html', {'services': services})

@login_required
def add_service(request):
    if request.method == 'POST':
        form = ServiceForm(request.POST)
        if form.is_valid():
            service = form.save(commit=False)
            service.provider = request.user.provider
            service.save()
            return redirect('providers:manage_services')  # Updated with namespace
    else:
        form = ServiceForm()
    return render(request, 'providers/add_service.html', {'form': form})

@login_required
def view_schedule(request):
    return render(request, 'providers/view_schedule.html')
