# Generated by Django 4.2.2 on 2023-07-03 17:23

import ckeditor.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateField(auto_now_add=True, verbose_name='تاریخ انتشار')),
                ('status', models.BooleanField(choices=[(True, 'فعال'), (False, 'غیرفعال')], default=True, verbose_name='وضعیت')),
                ('name', models.CharField(max_length=350, verbose_name='عنوان')),
            ],
            options={
                'verbose_name': 'دسته بندی',
                'verbose_name_plural': 'دسته بندی ها',
            },
        ),
        migrations.CreateModel(
            name='ImageSlider',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateField(auto_now_add=True, verbose_name='تاریخ انتشار')),
                ('status', models.BooleanField(choices=[(True, 'فعال'), (False, 'غیرفعال')], default=True, verbose_name='وضعیت')),
                ('image', models.ImageField(upload_to='images/portfolio/', verbose_name='تصاویر')),
            ],
            options={
                'verbose_name': 'تصویر نمونه کار',
                'verbose_name_plural': 'تصاویر نمونه کارها',
            },
        ),
        migrations.CreateModel(
            name='Portfolio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateField(auto_now_add=True, verbose_name='تاریخ انتشار')),
                ('status', models.BooleanField(choices=[(True, 'فعال'), (False, 'غیرفعال')], default=True, verbose_name='وضعیت')),
                ('image', models.ImageField(upload_to='images/portfolio/', verbose_name='تصویر پیشنمایش')),
                ('title', models.CharField(max_length=500, verbose_name='عنوان')),
                ('customer', models.CharField(max_length=300, verbose_name='مشتری')),
                ('description', ckeditor.fields.RichTextField(verbose_name='توضیحات')),
                ('slug', models.SlugField(allow_unicode=True, editable=False, null=True, unique=True)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='portfolio', to='blog.category', verbose_name='دسته بندی')),
                ('slider', models.ManyToManyField(to='blog.imageslider', verbose_name='تصاویر')),
            ],
            options={
                'verbose_name': 'نمونه کار',
                'verbose_name_plural': 'نمونه کارها',
            },
        ),
    ]