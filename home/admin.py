from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import CustomUser


class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = ("username", "rule", "email", "is_staff", "is_active",)
    list_filter = ("rule", "is_staff", "is_active",)
    fieldsets = (
        (None, {"fields": ("username", "email", "password")}),
        ("اطلاعات کاربری", {"fields": ("first_name", "last_name", "image", "location", "rule", "phone", "birth_date")}),
        ("شبکه های اجتماعی", {"fields": ("github", "twitter", "linkedin", "telegram", "instagram")}),
        ("Permissions", {"fields": ("is_staff", "is_active", "groups", "user_permissions")}),
    )
    add_fieldsets = (
        (None, {
            "classes": ("wide",),
            "fields": (
                "username", "email", "password1", "password2", "is_staff",
                "is_active", "groups", "user_permissions"
            )}
         ),
    )
    search_fields = ("username", "rule", "first_name", "last_name")
    ordering = ("-date_joined",)


admin.site.register(CustomUser, CustomUserAdmin)
