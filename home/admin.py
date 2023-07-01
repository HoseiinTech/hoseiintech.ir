from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from jalali_date.admin import ModelAdminJalaliMixin

from home.forms import CustomUserCreationForm, CustomUserChangeForm
from home import models
from blog.utils import jalali_converter


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
    list_filter = ("status",)
    fieldsets = (
        (None, {"fields": ("about", "icon", "service")}),
        ("مشتریان", {"fields": ("customer", "comment")}),
    )

    @admin.display(description='خدمات')
    def get_services(self, obj):
        return ' - '.join([service.title for service in obj.service.all()[:3]])

    @admin.display(description='مشتریان')
    def get_customers(self, obj):
        return ' - '.join([customer.title for customer in obj.customer.all()[:3]])

    @admin.display(description='نظرات مشتریان')
    def get_comments(self, obj):
        return ' - '.join([comment.name for comment in obj.comment.all()[:3]])


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


@admin.register(models.Resume)
class ResumeAdmin(admin.ModelAdmin):
    list_display = ("get_education", "get_experience", "get_skill", "status")
    list_editable = ("status",)
    list_filter = ("status",)
    fieldsets = (
        ("تحصیلات و تجربیات", {"fields": ("education", "experience")}),
        ("مهارت ها", {"fields": ("skill",)}),
        (None, {"fields": ("status",)}),
    )

    @admin.display(description='تحصیلات')
    def get_education(self, obj):
        return ' - '.join([education.title for education in obj.education.all()[:3]])

    @admin.display(description='تجربیات')
    def get_experience(self, obj):
        return ' - '.join([experience.title for experience in obj.experience.all()[:3]])

    @admin.display(description='مهارت ها')
    def get_skill(self, obj):
        return ' - '.join([skill.title for skill in obj.skill.all()[:3]])


@admin.register(models.Education)
class ExperienceAdmin(ModelAdminJalaliMixin, admin.ModelAdmin):
    list_display = ('title', 'of_year_jalali', 'until_year_jalali', 'status')
    list_filter = ('status', 'started_at', 'ended_at')
    list_editable = ('status',)

    search_fields = ('title', 'description')

    @admin.display(description='تاریخ شروع')
    def of_year_jalali(self, obj):
        return jalali_converter(obj.started_at)

    @admin.display(description='تاریخ پایان')
    def until_year_jalali(self, obj):
        return jalali_converter(obj.ended_at)


@admin.register(models.Experience)
class ExperienceAdmin(ModelAdminJalaliMixin, admin.ModelAdmin):
    list_display = ('title', 'of_year_jalali', 'until_year_jalali', 'status')
    list_filter = ('status', 'started_at', 'ended_at')
    list_editable = ('status',)

    search_fields = ('title', 'description')

    @admin.display(description='تاریخ شروع')
    def of_year_jalali(self, obj):
        return jalali_converter(obj.started_at)

    @admin.display(description='تاریخ پایان')
    def until_year_jalali(self, obj):
        return jalali_converter(obj.ended_at)


@admin.register(models.Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = ("title", "skill_percentage", "status")
    list_filter = ("status",)
    list_editable = ("status",)

    search_fields = ('title', "percentage")
