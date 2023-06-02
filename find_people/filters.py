from django.contrib.auth.models import User
from user_profile.models import UserInfo
import django_filters


class UserFilter(django_filters.FilterSet):
    class Meta:
        model = UserInfo
        fields = ['name', 'surname', 'gender']