# Generated by Django 4.1.6 on 2023-02-20 11:22

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("user_profile", "0002_userinfo_country_of_residence_alter_userinfo_gender"),
    ]

    operations = [
        migrations.AlterField(
            model_name="userinfo",
            name="login",
            field=models.OneToOneField(
                on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL
            ),
        ),
    ]
