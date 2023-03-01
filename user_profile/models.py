from django.db import models
from django.conf import settings


class UserInfo(models.Model):
    class Gender(models.TextChoices):
        male = "male"
        female = "female"
        different = "different"
        not_specified = "not_specified"

    login = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    gender = models.CharField(max_length=20, choices=Gender.choices, default=Gender.not_specified)
    email = models.EmailField()
    country_of_residence = models.CharField(max_length=100, default="not specified")
    user_avatar = models.URLField()
    user_description = models.TextField()










