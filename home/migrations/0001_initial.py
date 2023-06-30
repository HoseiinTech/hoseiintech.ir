# Generated by Django 4.2.2 on 2023-06-30 16:22

import django.contrib.auth.validators
from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('logo', models.ImageField(upload_to='images/icon/customers', verbose_name='لوگو')),
                ('title', models.CharField(max_length=200, verbose_name='عنوان')),
                ('url', models.URLField(blank=True, max_length=250, null=True, verbose_name='آدرس اینترنتی')),
                ('status', models.BooleanField(choices=[(True, 'فعال'), (False, 'غیرفعال')], default=True, verbose_name='وضعیت')),
            ],
            options={
                'verbose_name': 'مشتری',
                'verbose_name_plural': 'مشتریان',
            },
        ),
        migrations.CreateModel(
            name='CustomerComment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='نام')),
                ('profile', models.ImageField(upload_to='images/profile/customers/', verbose_name='عکس پروفایل')),
                ('text', models.CharField(max_length=400, verbose_name='نظر')),
                ('full_text', models.TextField(blank=True, null=True, verbose_name='نظر کامل')),
                ('date', models.DateTimeField(verbose_name='تاریخ نظر')),
                ('status', models.BooleanField(choices=[(True, 'فعال'), (False, 'غیرفعال')], default=True, verbose_name='وضعیت')),
            ],
            options={
                'verbose_name': 'نظر مشتری',
                'verbose_name_plural': 'نظرات مشتریان',
            },
        ),
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='عنوان')),
                ('icon', models.ImageField(blank=True, null=True, upload_to='images/icon/services/', verbose_name='آیکون')),
                ('description', models.TextField(verbose_name='توضیحات')),
                ('status', models.BooleanField(choices=[(True, 'فعال'), (False, 'غیرفعال')], default=True, verbose_name='وضعیت')),
            ],
            options={
                'verbose_name': 'خدمت',
                'verbose_name_plural': 'خدمات',
            },
        ),
        migrations.CreateModel(
            name='AboutMe',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('about', models.TextField(verbose_name='درباره من')),
                ('status', models.BooleanField(blank=True, choices=[(True, 'فعال'), (False, 'غیرفعال')], default=True, null=True, verbose_name='وضعیت')),
                ('comment', models.ManyToManyField(blank=True, limit_choices_to={'status': True}, to='home.customercomment', verbose_name='نظرات')),
                ('customer', models.ManyToManyField(blank=True, limit_choices_to={'status': True}, to='home.customer', verbose_name='مشتریان')),
                ('service', models.ManyToManyField(blank=True, limit_choices_to={'status': True}, to='home.service', verbose_name='خدمات')),
            ],
            options={
                'verbose_name': 'درباره من',
                'verbose_name_plural': 'درباره من',
            },
        ),
        migrations.CreateModel(
            name='CustomUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('image', models.ImageField(blank=True, null=True, upload_to='images/profile/', verbose_name='عکس کاربر')),
                ('rule', models.CharField(blank=True, choices=[('توسعه دهنده وب', 'توسعه دهنده وب'), ('توسعه دهنده بک اند', 'توسعه دهنده بک اند'), ('توسعه دهنده فرانت اند', 'توسعه دهنده فرانت اند'), ('توسعه دهنده اندروید', 'توسعه دهنده اندروید'), ('برنامه نویس', 'برنامه نویس'), ('دیگر دسته ها', 'دیگر دسته ها')], max_length=100, null=True, verbose_name='نقش')),
                ('phone', models.CharField(blank=True, max_length=10, null=True, verbose_name='شماره همراه')),
                ('birth_date', models.DateField(blank=True, null=True, verbose_name='تاریخ تولد')),
                ('location', models.CharField(default='ایران، تهران', max_length=150, verbose_name='موقعیت مکانی')),
                ('github', models.URLField(blank=True, max_length=300, null=True, verbose_name='آدرس گیت هاب')),
                ('instagram', models.URLField(blank=True, max_length=300, null=True, verbose_name='آدرس اینستاگرام')),
                ('telegram', models.URLField(blank=True, max_length=300, null=True, verbose_name='آدرس تلگرام')),
                ('twitter', models.URLField(blank=True, max_length=400, null=True, verbose_name='آدرس توییتر')),
                ('linkedin', models.URLField(blank=True, max_length=400, null=True, verbose_name='آدرس لینکدین')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'کاربر',
                'verbose_name_plural': 'کاربر ها',
            },
        ),
    ]
