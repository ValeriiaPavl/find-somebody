from django.contrib.auth import forms
#from .models import User
from django.contrib.auth import get_user_model


class RegistrationForm(forms.UserCreationForm):

    class Meta:
        User = get_user_model()
        model = User
        fields = ['username', 'password1', 'password2']



