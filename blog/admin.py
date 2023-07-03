from django.contrib import admin
from django.utils.html import format_html

from blog import models


@admin.register(models.Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'status']
    list_editable = ['status']
    list_filter = ['status']
    search_fields = ['name']


@admin.register(models.ImageSlider)
class ImageSliderAdmin(admin.ModelAdmin):
    list_display = ['get_image', 'status']
    list_editable = ['status']
    list_filter = ['status']

    @admin.display(description='تصویر')
    def get_image(self, obj):
        return format_html(
            f'<img src="{obj.image.url}" style="height:40px;width:15;border-radius:3px;"')


class ImageSliderInline(admin.TabularInline):
    model = models.Portfolio.slider.through
    extra = 1
    verbose_name = 'تصویر نمونه کار'
    verbose_name_plural = 'افزودن تصویر نمونه کار'


@admin.register(models.Portfolio)
class PortfolioAdmin(admin.ModelAdmin):
    list_display = ['get_image', 'title', 'customer', 'category', 'status']
    list_editable = ['status']
    list_filter = ['status', 'category']
    search_fields = ['title', 'category', 'description', 'customer']
    inlines = [ImageSliderInline]
    fieldsets = (
        ("جزئیات نمونه کار", {"fields": ("status", "title", "customer", "category", "image", "description")}),
    )

    @admin.display(description='تصویر پیشنمایش')
    def get_image(self, obj):
        return format_html(
            f'<img src="{obj.image.url}" style="height:40px;width:15;border-radius:3px;"')
