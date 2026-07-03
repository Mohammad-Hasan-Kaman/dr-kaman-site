from django.db import models
from django.core.validators import FileExtensionValidator


class Book(models.Model):
    title = models.CharField(max_length=200, verbose_name="عنوان کتاب")
    description = models.TextField(blank=True, null=True, verbose_name="توضیحات")

    cover_image = models.ImageField(
        upload_to='book_covers/',
        verbose_name="تصویر جلد",
        validators=[FileExtensionValidator(allowed_extensions=['jpg', 'jpeg', 'png', 'webp'])]
    )

    book_file = models.FileField(
        upload_to='books/',
        verbose_name="فایل کتاب (PDF)",
        validators=[FileExtensionValidator(allowed_extensions=['pdf', 'epub'])]
    )

    created_at = models.DateTimeField(auto_now_add=True, verbose_name="تاریخ ایجاد")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "کتاب"
        verbose_name_plural = "کتاب‌ها"