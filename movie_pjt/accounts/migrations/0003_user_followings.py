# Generated by Django 2.1.8 on 2019-04-20 13:47

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_user_follwers'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='followings',
            field=models.ManyToManyField(related_name='user_followings_user', to=settings.AUTH_USER_MODEL),
        ),
    ]
