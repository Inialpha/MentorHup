# Generated by Django 5.0.4 on 2024-04-11 15:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('career_link', '0008_alter_channel_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='channel',
            name='price',
            field=models.DecimalField(decimal_places=2, max_digits=10, null=True),
        ),
    ]
