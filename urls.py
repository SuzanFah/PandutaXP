from django.contrib import admin
from django.urls import path, include  # include is already imported here

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', core_views.home, name='home'),
    
    # Client URLs with namespace
    path('clients/', include('apps.clients.urls', namespace='clients')),
    
    # Provider URLs with namespace
    path('providers/', include('apps.providers.urls', namespace='providers')),
    path('providers/signup/', provider_signup, name='provider_signup'),
    
    # Authentication URLs
    path('accounts/login/', CustomLoginView.as_view(), name='login'),
    path('accounts/logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('register/', account_views.register_view, name='register'),
]

