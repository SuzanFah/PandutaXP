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