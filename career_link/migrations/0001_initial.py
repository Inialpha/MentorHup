# Generated by Django 5.0.4 on 2024-04-09 15:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('firstname', models.CharField(max_length=255)),
                ('lastname', models.CharField(max_length=255)),
                ('password', models.CharField(max_length=255)),
                ('role', models.CharField(choices=[('Mentor', 'Mentor'), ('Mentee', 'Mentee')], max_length=60)),
                ('profile_picture', models.ImageField(upload_to='')),
                ('bio', models.CharField(max_length=1024)),
                ('email', models.EmailField(max_length=255, unique=True)),
                ('category', models.CharField(choices=[('Software Engineer', 'Software Engineer')], max_length=255)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
