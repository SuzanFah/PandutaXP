from django.shortcuts import render

# Create your views here.
def provider_dashboard(request):
    context = {
        'title': 'Provider Dashboard',
        'orders': ['Order 1', 'Order 2', 'Order 3']  # Sample data
    }
    return render(request, 'providers/dashboard.html', context)

def manage_orders(request):
    return render(request, 'providers/manage_orders.html')

from django.shortcuts import render, redirect
from .forms import ProviderSignUpForm

def provider_signup(request):
    if request.method == 'POST':
        form = ProviderSignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            return redirect('login')
    else:
        form = ProviderSignUpForm()
    return render(request, 'providers/signup.html', {'form': form})
