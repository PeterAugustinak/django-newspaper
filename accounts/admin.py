from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import CustomUser


class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser

    list_display = [
        "email",
        "username",
        "age",
        "is_staff",
        ]

    # additional field for create user form
    add_fieldsets = UserAdmin.add_fieldsets + ((None, {"fields": ("age",)}),)
    # additional field for edit user form
    fieldsets = UserAdmin.fieldsets + ((None, {"fields": ("age",)}),)


admin.site.register(CustomUser, CustomUserAdmin)
