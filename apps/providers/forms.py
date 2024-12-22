from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Provider

class ProviderSignUpForm(UserCreationForm):
    phone = forms.CharField(max_length=15)
    address = forms.CharField(widget=forms.Textarea)
    service_type = forms.CharField(max_length=100)

    class Meta:
        model = User
        fields = ('username', 'password1', 'password2', 'phone', 'address', 'service_type')
