# audios/models.py

from django.db import models
from categories.models import Category
from django.core.validators import FileExtensionValidator  # <-- این خط را اضافه کنید


class AudioWork(models.Model):
    title = models.CharField(max_length=200, verbose_name="عنوان")
    description = models.TextField(blank=True, null=True, verbose_name="توضیحات")

    # --- اعتبارسنجی به این فیلد اضافه شده است ---
    audio_file = models.FileField(
        upload_to='audios/',
        verbose_name="فایل صوتی",
        validators=[FileExtensionValidator(allowed_extensions=['mp3', 'wav', 'ogg', 'm4a', 'mp4'])]
    )

    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True, verbose_name="دسته‌بندی")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="تاریخ ایجاد")

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        from django.urls import reverse
        return reverse('audios:audio_list') + f'?id={self.id}'