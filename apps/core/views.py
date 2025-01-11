from django.shortcuts import render
from django.conf import settings
import os

def home(request):
    # Add profile image path
    profile_image = os.path.join(settings.STATIC_URL, 'images/pandutadefault.png')
    return render(request, 'core/home.html', {'profile_image': profile_image})

def about_view(request):
    return render(request, 'core/about.html')

def services_view(request):
    return render(request, 'core/services.html')

def contact_view(request):
    return render(request, 'core/contact.html')