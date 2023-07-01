from decimal import Decimal
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.html import format_html
from django.core.validators import MinValueValidator, MaxValueValidator

from home.managers import CustomUserManager
from blog.utils import jalali_converter, jalali_formatted_converter

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
    icon = models.FileField(upload_to='images/icon/site/', verbose_name='آیکون وبسایت', null=True, blank=True)
    service = models.ManyToManyField('Service', verbose_name='خدمات', limit_choices_to={"status": True}, blank=True)
    customer = models.ManyToManyField('Customer', verbose_name='مشتریان', limit_choices_to={"status": True}, blank=True)
    comment = models.ManyToManyField('CustomerComment', verbose_name='نظرات', limit_choices_to={"status": True},
                                     blank=True)
    status = models.BooleanField(default=True, verbose_name='وضعیت', choices=STATUS_CHOICES)

    class Meta:
        verbose_name = 'درباره من'
        verbose_name_plural = 'درباره من'

    def __str__(self):
        return f"درباره من - شماره {self.id}"


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


class Resume(models.Model):
    education = models.ManyToManyField('Education', verbose_name='تحصیلات', limit_choices_to={'status': True},
                                       blank=True)
    experience = models.ManyToManyField('Experience', verbose_name='تجربیات', limit_choices_to={'status': True},
                                        blank=True)
    skill = models.ManyToManyField('Skill', verbose_name='مهارت ها', limit_choices_to={'status': True},
                                   blank=True)
    status = models.BooleanField(choices=STATUS_CHOICES, default=True, verbose_name='وضعیت')

    class Meta:
        verbose_name = 'رزومه'
        verbose_name_plural = 'رزومه من'

    def __str__(self):
        return f"رزومه من - شماره {self.id}"


JALALIDATE_HELP = 'روی فیلد کلیک کنید، و سپس تاریخ خود را به طور فارسی انتخاب کنید'


class Education(models.Model):
    title = models.CharField(max_length=300, verbose_name='عنوان')
    started_at = models.DateField(verbose_name='تاریخ شروع', help_text=JALALIDATE_HELP)
    ended_at = models.DateField(verbose_name='تاریخ پایان', help_text=JALALIDATE_HELP)
    description = models.TextField(verbose_name='توضیحات')
    status = models.BooleanField(choices=STATUS_CHOICES, default=True, verbose_name='وضعیت')

    class Meta:
        verbose_name = 'تحصیلات'
        verbose_name_plural = 'تحصیلات'

    def __str__(self):
        return self.title

    def date_jalali(self):
        started = jalali_formatted_converter(self.started_at)
        ended = jalali_formatted_converter(self.ended_at)
        return f"{started} - {ended}"


class Experience(models.Model):
    title = models.CharField(max_length=300, verbose_name='عنوان')
    started_at = models.DateField(verbose_name='تاریخ شروع', help_text=JALALIDATE_HELP)
    ended_at = models.DateField(verbose_name='تاریخ پایان', help_text=JALALIDATE_HELP)
    description = models.TextField(verbose_name='توضیحات')
    status = models.BooleanField(choices=STATUS_CHOICES, default=True, verbose_name='وضعیت')

    class Meta:
        verbose_name = 'تجربه'
        verbose_name_plural = 'تجربیات'

    def __str__(self):
        return self.title

    def date_jalali(self):
        started = jalali_formatted_converter(self.started_at)
        ended = jalali_formatted_converter(self.ended_at)
        return f"{started} - {ended}"


PERCENTAGE_VALIDATOR = [MinValueValidator(0), MaxValueValidator(100)]


class Skill(models.Model):
    title = models.CharField(max_length=350, verbose_name='عنوان')
    percentage = models.DecimalField(max_digits=3, decimal_places=0, default=Decimal(0),
                                     validators=PERCENTAGE_VALIDATOR, verbose_name='درصد مهارت')
    status = models.BooleanField(choices=STATUS_CHOICES, default=True, verbose_name='وضعیت')

    class Meta:
        verbose_name = 'مهارت'
        verbose_name_plural = 'مهارت ها'

    def __str__(self):
        return self.title

    def skill_percentage(self):
        return format_html(
            f'''
            <progress value="{self.percentage}" max="100"></progress>
            <span style="font-weight:bold">{self.percentage}%</span>
            ''',
        )

    skill_percentage.short_description = 'درصد مهارت'
