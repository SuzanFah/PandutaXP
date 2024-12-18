from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from apps.core import views
from apps.clients.views import client_signup, client_dashboard
from apps.providers.views import provider_signup, provider_dashboard


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('clients/', include('apps.clients.urls')),
    path('providers/', include('apps.providers.urls')),
    path('clients/signup/', client_signup, name='client_signup'),
    path('providers/signup/', provider_signup, name='provider_signup'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('clients/dashboard/', client_dashboard, name='client_dashboard'),
    path('providers/dashboard/', provider_dashboard, name='provider_dashboard'),
    path('accounts/login/', auth_views.LoginView.as_view(), name='login'),
    path('accounts/logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('accounts/password_reset/', auth_views.PasswordResetView.as_view(), name='password_reset'),
    path('accounts/password_reset/done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('accounts/reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('accounts/reset/done/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
]