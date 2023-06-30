from django.contrib.auth.models import AbstractUser
from django.db import models

from home.managers import CustomUserManager

RULE_CHOICES = (
    ('توسعه دهنده وب', 'توسعه دهنده وب'),
    ('توسعه دهنده بک اند', 'توسعه دهنده بک اند'),
    ('توسعه دهنده فرانت اند', 'توسعه دهنده فرانت اند'),
    ('توسعه دهنده اندروید', 'توسعه دهنده اندروید'),
    ('برنامه نویس', 'برنامه نویس'),
    ('دیگر دسته ها', 'دیگر دسته ها'),
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
