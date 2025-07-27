# core/models.py

from django.db import models

# مدل جدید و اختصاصی برای مدیریت تصاویر اسلایدر
class Slider(models.Model):
    title = models.CharField(max_length=200, verbose_name="عنوان اسلاید")
    description = models.TextField(blank=True, null=True, verbose_name="توضیحات کوتاه")
    image = models.ImageField(upload_to='sliders/', verbose_name="تصویر اسلایدر")
    link = models.URLField(blank=True, null=True, verbose_name="لینک (اختیاری)")
    is_active = models.BooleanField(default=True, verbose_name="فعال باشد؟")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "اسلاید"
        verbose_name_plural = "اسلایدها"