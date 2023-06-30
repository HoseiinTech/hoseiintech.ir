from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from home.forms import CustomUserCreationForm, CustomUserChangeForm
from home import models


class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = models.Customer
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


admin.site.register(models.CustomUser, CustomUserAdmin)


@admin.register(models.AboutMe)
class AboutAdmin(admin.ModelAdmin):
    list_display = ("get_services", "get_customers", "get_comments", "status")
    list_editable = ("status",)
    fieldsets = (
        (None, {"fields": ("about", "service")}),
        ("مشتریان", {"fields": ("customer", "comment")}),
    )


@admin.register(models.Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ("title", "status")
    list_editable = ("status",)
    list_filter = ("status",)
    search_fields = ("title", "description")


@admin.register(models.Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ("get_image", "title", "status")
    list_editable = ("status",)
    list_filter = ("status",)
    search_fields = ("title",)


@admin.register(models.CustomerComment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ("get_image", "name", "jalali_date", "status")
    list_editable = ("status",)
    list_filter = ("status", "date")
    search_fields = ("name", "text")
