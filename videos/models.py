# videos/models.py

from django.db import models
from categories.models import Category
from django.core.validators import FileExtensionValidator  # <-- این خط را اضافه کنید


class VideoWork(models.Model):
    title = models.CharField(max_length=200, verbose_name="عنوان")
    description = models.TextField(blank=True, null=True, verbose_name="توضیحات")

    # --- اعتبارسنجی به این فیلد اضافه شده است ---
    video_file = models.FileField(
        upload_to='videos/',
        verbose_name="فایل ویدیویی",
        validators=[FileExtensionValidator(allowed_extensions=['mp4', 'mkv', 'mov', 'avi', 'webm'])]
    )

    slider_image = models.ImageField(
        upload_to='slider_images/',
        verbose_name="تصویر برای اسلایدر (اختیاری)",
        null=True,
        blank=True,
        validators=[FileExtensionValidator(allowed_extensions=['jpg', 'jpeg', 'png', 'webp'])]
    )

    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True, verbose_name="دسته‌بندی")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="تاریخ ایجاد")

    def __str__(self):
        return self.title