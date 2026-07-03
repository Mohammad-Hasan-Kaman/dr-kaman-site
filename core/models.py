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


# مدل برای محتوای صفحه درباره (داینامیک)
class AboutPage(models.Model):
    title = models.CharField(max_length=200, default="درباره دکتر محمد رضا کمن", verbose_name="عنوان صفحه")
    content = models.TextField(verbose_name="محتوای صفحه درباره")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="تاریخ آخرین بروزرسانی")

    class Meta:
        verbose_name = "صفحه درباره"
        verbose_name_plural = "صفحه درباره"

    def __str__(self):
        return self.title


# مدل برای محتوای صفحه تماس (داینامیک)
class ContactPage(models.Model):
    title = models.CharField(max_length=200, default="تماس با ما", verbose_name="عنوان صفحه")
    content = models.TextField(verbose_name="محتوای صفحه تماس")
    phone = models.CharField(max_length=20, blank=True, verbose_name="شماره تلفن")
    email = models.EmailField(blank=True, verbose_name="ایمیل")
    address = models.TextField(blank=True, verbose_name="آدرس")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="تاریخ آخرین بروزرسانی")

    class Meta:
        verbose_name = "صفحه تماس"
        verbose_name_plural = "صفحه تماس"

    def __str__(self):
        return self.title