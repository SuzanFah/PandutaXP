from django.urls import path
from . import views

app_name = 'clients'
urlpatterns = [
    path('', views.client_dashboard, name='dashboard'),
    path('track-order/', views.track_order, name='track_order'),
    path('dashboard/', views.client_dashboard, name='client_dashboard'),
    path('profile/', views.client_profile, name='client_profile'),
    path('services/', views.book_service, name='book_service'),
    path('services/<int:service_id>/book/', views.create_order, name='create_order'),
]
