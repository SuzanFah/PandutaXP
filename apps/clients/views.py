from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .forms import ClientSignUpForm
from .models import Client

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
    return render(request, 'clients/dashboard.html')
@login_required
def client_profile(request):
    return render(request, 'clients/profile.html')

@login_required
def book_service(request):
    return render(request, 'clients/book_service.html')

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
    return render(request, 'registration/register.html', {'form': form})\
        