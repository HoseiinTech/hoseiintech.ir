from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.html import format_html

from home.managers import CustomUserManager
from blog.utils import jalali_converter

RULE_CHOICES = (
    ('توسعه دهنده وب', 'توسعه دهنده وب'),
    ('توسعه دهنده بک اند', 'توسعه دهنده بک اند'),
    ('توسعه دهنده فرانت اند', 'توسعه دهنده فرانت اند'),
    ('توسعه دهنده اندروید', 'توسعه دهنده اندروید'),
    ('برنامه نویس', 'برنامه نویس'),
    ('دیگر دسته ها', 'دیگر دسته ها'),
)

STATUS_CHOICES = (
    (True, "فعال"),
    (False, "غیرفعال")
)


class CustomUser(AbstractUser):
    image = models.ImageField(upload_to='images/profile/', verbose_name='عکس کاربر', null=True, blank=True)
    rule = models.CharField(max_length=100, choices=RULE_CHOICES, verbose_name='نقش', null=True, blank=True)
    phone = models.CharField(max_length=10, verbose_name='شماره همراه', null=True, blank=True)
    birth_date = models.DateField(verbose_name='تاریخ تولد', null=True, blank=True)
    location = models.CharField(max_length=150, default='ایران، تهران', verbose_name='موقعیت مکانی')
    # SocialMedia Fields
    github = models.URLField(max_length=300, verbose_name='آدرس گیت هاب', null=True, blank=True)
    instagram = models.URLField(max_length=300, verbose_name='آدرس اینستاگرام', null=True, blank=True)
    telegram = models.URLField(max_length=300, verbose_name='آدرس تلگرام', null=True, blank=True)
    twitter = models.URLField(max_length=400, verbose_name='آدرس توییتر', null=True, blank=True)
    linkedin = models.URLField(max_length=400, verbose_name='آدرس لینکدین', null=True, blank=True)

    USERNAME_FIELD = "username"
    REQUIRED_FIELDS = ['email']

    objects = CustomUserManager()

    class Meta:
        verbose_name = 'کاربر'
        verbose_name_plural = 'کاربر ها'

    def __str__(self):
        if self.first_name or self.last_name:
            return self.get_full_name()
        return self.username


class AboutMe(models.Model):
    about = models.TextField(verbose_name='درباره من')
    service = models.ManyToManyField('Service', verbose_name='خدمات', limit_choices_to={"status": True}, blank=True)
    customer = models.ManyToManyField('Customer', verbose_name='مشتریان', limit_choices_to={"status": True}, blank=True)
    comment = models.ManyToManyField('CustomerComment', verbose_name='نظرات', limit_choices_to={"status": True},
                                     blank=True)
    status = models.BooleanField(default=True, verbose_name='وضعیت', choices=STATUS_CHOICES, null=True, blank=True)

    class Meta:
        verbose_name = 'درباره من'
        verbose_name_plural = 'درباره من'

    def __str__(self):
        return "درباره من"

    def get_services(self):
        return ' - '.join([service.title for service in self.service.all()[:3]])

    get_services.short_description = 'خدمات'

    def get_customers(self):
        return ' - '.join([customer.title for customer in self.customer.all()[:3]])

    get_customers.short_description = 'مشتریان'

    def get_comments(self):
        return ' - '.join([comment.name for comment in self.comment.all()[:3]])

    get_comments.short_description = 'نظرات مشتریان'


class Service(models.Model):
    title = models.CharField(max_length=200, verbose_name='عنوان')
    icon = models.ImageField(upload_to='images/icon/services/', verbose_name='آیکون', null=True, blank=True)
    description = models.TextField(verbose_name='توضیحات')
    status = models.BooleanField(default=True, verbose_name='وضعیت', choices=STATUS_CHOICES)

    class Meta:
        verbose_name = 'خدمت'
        verbose_name_plural = 'خدمات'

    def __str__(self):
        return f"{self.title}"


class Customer(models.Model):
    logo = models.ImageField(upload_to='images/icon/customers', verbose_name='لوگو')
    title = models.CharField(max_length=200, verbose_name='عنوان')
    url = models.URLField(max_length=250, verbose_name='آدرس اینترنتی', null=True, blank=True)
    status = models.BooleanField(default=True, verbose_name='وضعیت', choices=STATUS_CHOICES)

    class Meta:
        verbose_name = 'مشتری'
        verbose_name_plural = 'مشتریان'

    def __str__(self):
        return self.title

    def get_image(self):
        return format_html(
            f'<img src="{self.logo.url}" alt="{self.title}" style="height:35px;width:35px;border-radius:3px;"')

    get_image.short_description = 'لوگو'


class CustomerComment(models.Model):
    name = models.CharField(max_length=200, verbose_name='نام')
    profile = models.ImageField(upload_to='images/profile/customers/', verbose_name='عکس پروفایل')
    text = models.CharField(max_length=400, verbose_name='نظر')
    full_text = models.TextField(verbose_name='نظر کامل', null=True, blank=True)
    date = models.DateTimeField(verbose_name='تاریخ نظر')
    status = models.BooleanField(default=True, verbose_name='وضعیت', choices=STATUS_CHOICES)

    class Meta:
        verbose_name = 'نظر مشتری'
        verbose_name_plural = 'نظرات مشتریان'

    def __str__(self):
        return f"{self.name}"

    def get_image(self):
        return format_html(
            f'<img src="{self.profile.url}" alt="{self.name}" style="height:50px;width:50px;border-radius:3px;"')

    get_image.short_description = 'عکس پروفایل'

    def jalali_date(self):
        return jalali_converter(self.date)

    jalali_date.short_description = 'تاریخ نظر'
