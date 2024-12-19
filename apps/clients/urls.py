from django.urls import path
from . import views

app_name = 'clients'
urlpatterns = [
    path('', views.client_dashboard, name='dashboard'),
    path('book-service/', views.book_service, name='book_service'),
    path('track-order/', views.track_order, name='track_order'),
]