from django import forms    
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, BaseUserCreationForm
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



class UserCreationForm(BaseUserCreationForm):
    def clean_username(self):
        """Reject usernames that differ only in case."""
        username = self.cleaned_data.get("username")
        if (
            username
            and self._meta.model.objects.filter(username__iexact=username).exists()
        ):
            self._update_errors(
                ValidationError(
                    {
                        "username": self.instance.unique_error_message(
                            self._meta.model, ["username"]
                        )
                    }
                )
            )
        else:
            return username
        
# """ https://github.com/django/django/blob/main/django/contrib/auth/forms.py#L152"""