from django import forms
from django.contrib.auth.forms import UserCreationForm 
from django.contrib.auth.models import User

class CustomUserForm(UserCreationForm):
    color=forms.CharField(max_length=100)
    class Meta:
        model=User
        fields=['first_name','last_name','username','email','color']

        