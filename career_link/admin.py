from django.contrib import admin
from .models import User
from django.contrib.auth.admin import UserAdmin
from authemail.admin import EmailUserAdmin
from django.contrib.auth import get_user_model
class CustomUserAdmin(EmailUserAdmin):
    model = User
    # Add any additional fields you want to display in the admin panel
    list_filter = ["is_staff"]
    list_display = ['email', 'first_name', 'last_name', 'is_staff']
    fieldsets = [
        (None, {"fields": ["email", "password"]}),
        ("Personal info", {"fields": ["first_name", "last_name"]}),
        ("Permissions", {"fields": ["is_staff"]}),
    ]
    add_fieldsets = [
        (
            None,
            {
                "classes": ["wide"],
                "fields": ["email", "first_name", "last_name", "password1", "password2"],
            },
        ),
    ]
    ordering = ["first_name"]
    # Add any fieldsets customization if needed

admin.site.unregister(get_user_model())
admin.site.register(User, CustomUserAdmin)
