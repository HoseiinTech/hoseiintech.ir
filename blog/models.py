from django.db import models
from django.utils.text import slugify
from django.urls import reverse

from ckeditor.fields import RichTextField
from blog.utils import jalali_converter

STATUS_CHOICES = (
    (True, "فعال"),
    (False, "غیرفعال")
)


class BaseModel(models.Model):
    created_at = models.DateField(auto_now_add=True, verbose_name='تاریخ انتشار')
    status = models.BooleanField(default=True, verbose_name='وضعیت', choices=STATUS_CHOICES)

    class Meta:
        abstract = True


class Portfolio(BaseModel):
    image = models.ImageField(upload_to='images/portfolio/', verbose_name='تصویر پیشنمایش')
    title = models.CharField(max_length=500, verbose_name='عنوان')
    customer = models.CharField(max_length=300, verbose_name='مشتری')
    category = models.ForeignKey('Category', on_delete=models.CASCADE, related_name='portfolio',
                                 verbose_name='دسته بندی')
    description = RichTextField(verbose_name='توضیحات')
    slider = models.ManyToManyField('ImageSlider', verbose_name='تصاویر')
    slug = models.SlugField(unique=True, null=True, editable=False, allow_unicode=True)

    class Meta:
        verbose_name = 'نمونه کار'
        verbose_name_plural = 'نمونه کارها'

    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        self.slug = slugify(self.title, allow_unicode=True)
        super(Portfolio, self).save()

    def __str__(self):
        return f"{self.title} - {self.category}"

    def get_jalali_date(self):
        return jalali_converter(self.created_at)

    def get_absolute_url(self):
        return reverse('blog:project-detail', args=[self.slug])


class ImageSlider(BaseModel):
    image = models.ImageField(upload_to='images/portfolio/', verbose_name='تصاویر')

    class Meta:
        verbose_name_plural = 'تصاویر نمونه کارها'
        verbose_name = 'تصویر نمونه کار'

    def __str__(self):
        return f"تصویر شماره {self.id}"


class Category(BaseModel):
    name = models.CharField(max_length=350, verbose_name='عنوان')

    class Meta:
        verbose_name = 'دسته بندی'
        verbose_name_plural = 'دسته بندی ها'

    def __str__(self):
        return self.name
