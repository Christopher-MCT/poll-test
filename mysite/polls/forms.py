from django import forms    
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


from django.utils.translation import gettext_lazy as _


class LoginForm(forms.Form):
    username = forms.CharField(max_length=65)
    password = forms.CharField(max_length=65, widget=forms.PasswordInput)
     