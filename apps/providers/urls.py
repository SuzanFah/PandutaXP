from django.urls import path
from . import views

app_name = 'providers'

urlpatterns = [
    path('', views.provider_dashboard, name='dashboard'),
    path('signup/', views.provider_signup, name='provider_signup'),
    path('login/', views.provider_login, name='provider_login'),
    path('dashboard/', views.provider_dashboard, name='provider_dashboard'),
    path('update-status/', views.update_status, name='update_status'),
    path('view-schedule/', views.view_schedule, name='view_schedule'),
    path('services/', views.manage_services, name='manage_services'),
    path('services/add/', views.add_service, name='add_service'),
]

