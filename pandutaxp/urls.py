from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from apps.core import views as core_views
from apps.clients.views import client_dashboard
from apps.providers.views import provider_dashboard, provider_signup
from accounts import views as account_views
from accounts.views import CustomLoginView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', core_views.home, name='home'),
   
    # Client URLs
    path('clients/', include('apps.clients.urls')),
    path('clients/dashboard/', client_dashboard, name='clients_dashboard'),
    # Provider URLs
    path('providers/', include('apps.providers.urls')),
    path('providers/dashboard/', provider_dashboard, name='providers_dashboard'),
    path('providers/signup/', provider_signup, name='provider_signup'),

    # Single authentication entry point
    path('accounts/login/', CustomLoginView.as_view(), name='login'),
   
    # Authentication URLs
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('register/', account_views.register_view, name='register'),
]