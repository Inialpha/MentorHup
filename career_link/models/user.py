from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from authemail.models import EmailUserManager, EmailAbstractUser

class UserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self.create_user(email, password, **extra_fields)


class User(EmailAbstractUser, PermissionsMixin):
    ROLES = {
        "Mentor": "Mentor",
        "Mentee": "Mentee"
    }

    CATEGORIES = {
        "Software Engineer": "Software Engineer"
    }
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    role = models.CharField(max_length=60, choices=ROLES)
    profile_picture = models.ImageField()
    bio = models.CharField(max_length=1024)
    email = models.EmailField(max_length=255, unique=True)
    categories = models.CharField(max_length=255, choices=CATEGORIES)
    is_staff = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name']  # Add any additional required fields

    objects = EmailUserManager()

    def has_perms(self, perm, obj=None):
        return self.is_superuser

    def has_module_perms(self, app_label):
        # Assume all users have permissions to all modules for simplicity
        return True
