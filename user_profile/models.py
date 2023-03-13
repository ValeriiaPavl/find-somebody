from django.db import models
from django.conf import settings
from django.db.models import QuerySet


class UserInfo(models.Model):
    class Sex(models.TextChoices):
        male = "male"
        female = "female"
        different = "different"
        not_specified = "not_specified"

    login = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    gender = models.CharField(max_length=20, choices=Sex.choices, default=Sex.not_specified)
    email = models.EmailField()
    country_of_residence = models.CharField(max_length=100, default="not specified")
    user_avatar = models.URLField()
    user_description = models.TextField()
    liked_users = models.ManyToManyField("self", symmetrical=False)

    @staticmethod
    def user_liked(pk: int, profiles_list: QuerySet) -> QuerySet:
        current_user_likes = UserInfo.objects.get(login=pk).liked_users.all()
        profiles_with_likes = profiles_list.annotate(liked=models.Exists(current_user_likes.filter(login=models.OuterRef('login'))))
        return profiles_with_likes



