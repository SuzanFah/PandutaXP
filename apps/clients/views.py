from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required
def client_dashboard(request):
    return render(request, 'clients/dashboard.html')

@login_required
def client_profile(request):
    return render(request, 'clients/profile.html')

@login_required
def book_service(request):
    return render(request, 'clients/book_service.html')

def track_order(request):
    return render(request, 'clients/track_order.html')

