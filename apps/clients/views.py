from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import ClientSignUpForm
from .models import Client
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm
from apps.providers.models import Provider, Service  # Import Service model
from apps.service_orders.models import Order
from django.utils import timezone  # Add this import at the top
from django.http import JsonResponse  # Add this at the top with other imports


def client_signup(request):
    if request.method == 'POST':
        form = ClientSignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            Client.objects.create(
                user=user,
                phone=form.cleaned_data.get('phone'),
                address=form.cleaned_data.get('address')
            )
            return redirect('client_login')
    else:
        form = ClientSignUpForm()
    return render(request, 'clients/signup.html', {'form': form})

@login_required
def client_dashboard(request):
    if not hasattr(request.user, 'client'):
        return redirect('home')
    
    # Get search parameters
    search_query = request.GET.get('search', '')
    service_type = request.GET.get('service_type', '')
    
    # Base provider query
    providers = Provider.objects.all()
    
    if search_query:
        providers = providers.filter(
            Q(user__username__icontains=search_query) |
            Q(service_type__icontains=search_query)
        )
    
    context = {
        'providers': providers,
        'search_query': search_query,
    }
    return render(request, 'clients/dashboard.html', context)
import os
from django.conf import settings

def client_profile(request):
    # Add profile image path
    profile_image = os.path.join(settings.STATIC_URL, 'images/pandutadefault.png')
    return render(request, 'clients/profile.html', {'profile_image': profile_image})

@login_required
def book_service(request):
    services = Service.objects.filter(available=True)
    return render(request, 'clients/book_service.html', {'services': services})

@login_required
def create_order(request, service_id):
    try:
        service = Service.objects.get(id=service_id)
        Order.objects.create(
            client=request.user.client,
            service_type=service.name,
            pickup_time=timezone.now()
        )
        return redirect('clients:track_order')
    except Service.DoesNotExist:
        return redirect('clients:book_service')
def track_order(request):
    orders = Order.objects.filter(client=request.user.client)
    return render(request, 'clients/track_order.html', {'orders': orders})

# Authentication Views
def register_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'registration/register.html', {'form': form})

def client_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None and hasattr(user, 'client'):
                login(request, user)
                return redirect('clients:dashboard')
    else:
        form = AuthenticationForm()
    return render(request, 'clients/login.html', {'form': form})
