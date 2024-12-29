from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import ClientSignUpForm
from .models import Client
from orders.models import Order
from apps.providers.models import Provider

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
    return render(request, 'clients/dashboard.html', {'user': request.user})
def client_profile(request):
    return render(request, 'clients/profile.html')

@login_required
def book_service(request):
    services = Service.objects.filter(available=True)
    return render(request, 'clients/book_service.html', {'services': services})

@login_required
def create_order(request, service_id):
    service = Service.objects.get(id=service_id)
    order = Order.objects.create(
        client=request.user.client,
        service=service,
        scheduled_for=request.POST['scheduled_for'],
        total_price=service.price
    )
    return redirect('clients:track_order', order_id=order.id)

@login_required
def track_order(request):
    return render(request, 'clients/track_order.html')

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
