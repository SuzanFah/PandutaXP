from django.urls import path
from . import views

urlpatterns = [
    path('process/<int:order_id>/', views.process_payment, name='process_payment'),
    path('confirm/', views.payment_confirmation, name='payment_confirmation'),
]
