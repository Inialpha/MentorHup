# Generated by Django 5.0.4 on 2024-04-16 12:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('career_link', '0011_alter_user_options_user_date_joined_user_first_name_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='firstname',
        ),
        migrations.RemoveField(
            model_name='user',
            name='lastname',
        ),
        migrations.AlterField(
            model_name='user',
            name='first_name',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='user',
            name='last_name',
            field=models.CharField(max_length=255),
        ),
    ]
