# Generated by Django 5.0.4 on 2024-04-11 15:17

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('career_link', '0006_channel'),
    ]

    operations = [
        migrations.AlterField(
            model_name='channel',
            name='mentees',
            field=models.ManyToManyField(blank=True, to=settings.AUTH_USER_MODEL),
        ),
    ]