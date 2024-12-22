from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from apps.core import views as core_views
from apps.clients.views import client_dashboard
from apps.providers.views import provider_dashboard
from accounts import views as account_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', core_views.home, name='home'),
   
    # Client URLs
    path('clients/', include('apps.clients.urls')),
    path('clients/dashboard/', client_dashboard, name='client_dashboard'),
   
    # Client auth paths
    path('clients/login/', auth_views.LoginView.as_view(
        template_name='clients/login.html',
        success_url='client_dashboard'
    ), name='client_login'),
   
    # Provider URLs
    path('providers/', include('apps.providers.urls')),
    path('providers/dashboard/', provider_dashboard, name='provider_dashboard'),
   
    # Provider auth paths
    path('providers/login/', auth_views.LoginView.as_view(
        template_name='providers/login.html',
        success_url='provider_dashboard'
    ), name='provider_login'),
   
    # Authentication URLs
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('accounts/password_reset/', auth_views.PasswordResetView.as_view(), name='password_reset'),
    path('accounts/password_reset/done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('accounts/reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('accounts/reset/done/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
   
    # General URLs
    path('register/', account_views.register_view, name='register'),
]