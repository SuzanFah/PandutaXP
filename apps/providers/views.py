from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from .models import Provider
from .forms import ProviderSignUpForm

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
            return redirect('providers_dashboard')
    else:
        form = ProviderSignUpForm()
    return render(request, 'providers/signup.html', {'form': form})

@login_required
def provider_dashboard(request):
    return render(request, 'providers/dashboard.html')

def provider_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None and Provider.objects.filter(user=user).exists():
            login(request, user)
            return redirect('provider_dashboard')
    return render(request, 'providers/login.html')