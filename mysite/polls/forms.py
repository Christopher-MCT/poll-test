from django import forms    
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User




class SignupForm(UserCreationForm):
    f_name=forms.CharField(max_length=140, required=True)
    l_name=forms.CharField(max_length=140, required=   True)
    email = forms.EmailField(required=True)

    class Meta:
        model= User
        fields= (

            'username', 
            'email', 
            'f_name', 
            'l_name', 
            'password1',
            'password2',
        )



    