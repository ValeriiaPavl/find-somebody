from django import forms
from .models import UserInfo


class UserDescription(forms.ModelForm):
    avatar = forms.ImageField()

    class Meta:
        model = UserInfo
        exclude = ['user_avatar', 'login']