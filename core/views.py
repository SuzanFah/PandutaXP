from django.shortcuts import render

# Create your views here.

def services_view(request):
    return render(request, 'core/services.html')
