from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib.auth import login
from .forms import CustomRegistrationForm
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
@login_required
def dashboard_view(request):
    if hasattr(request.user, 'client'):
        return redirect('client_dashboard')
    elif hasattr(request.user, 'provider'):
        return redirect('provider_dashboard')
   
         