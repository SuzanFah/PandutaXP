from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required
def client_dashboard(request):
    return render(request, 'clients/dashboard.html')

@login_required
def client_profile(request):
    return render(request, 'clients/profile.html')

@login_required
def provider_dashboard(request):
    return render(request, 'providers/dashboard.html')

@login_required
def book_service(request):
    return render(request, 'clients/book_service.html')

def track_order(request):
    return render(request, 'clients/track_order.html')


from django.shortcuts import render, redirect
from .forms import ClientSignUpForm

def client_signup(request):
    if request.method == 'POST':
        form = ClientSignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            return redirect('login')
    else:
        form = ClientSignUpForm()
    return render(request, 'clients/signup.html', {'form': form})
