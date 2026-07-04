# 🧠 Dr. Kaman Psychology Portal

> یک آرشیو چندرسانه‌ای حرفه‌ای برای دکتر محمد رضا کمان، شامل پادکست‌ها، ویدیوها، کتاب‌ها و مقالات با قابلیت جستجوی پیشرفته.

[![Django](https://img.shields.io/badge/Django-4.2+-green.svg?logo=django&logoColor=white)](https://django.com)
[![Python](https://img.shields.io/badge/Python-3.10+-blue.svg?logo=python&logoColor=white)](https://python.org)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Release](https://img.shields.io/github/v/release/Mohammad-Hasan-Kaman/dr-kaman-site?color=blue)](https://github.com/Mohammad-Hasan-Kaman/dr-kaman-site/releases)

---

## 🚀 هدف و مخاطبان

این پروژه با رویکرد **"دسترسی آسان به محتوای روانشناسی"** طراحی شده است:

| مخاطب | روش استفاده |
|-------|--------------|
| **مراجعین & عموم مردم** | مراجعه به وب‌سایت مستقر شده (لینک LIVE در بخش Releases) برای دسترسی آسان به محتوا. |
| **توسعه‌دهندگان** | کلون کردن سورس کد، اجرا در محیط لوکال برای مطالعه، توسعه یا تغییرات. |

---

## ✨ ویژگی‌های کلیدی

- 🎨 **رابط کاربری مدرن با فونت فارسی:** استفاده از فونت `BMitra` برای نمایش صحیح و زیبای متون فارسی.
- 🎧 **آرشیو چندرسانه‌ای کامل:**
  - **پادکست‌ها (AudioWork):** فایل‌های صوتی با دسته‌بندی موضوعی.
  - **ویدیوها (VideoWork):** ویدیوهای آموزشی و سخنرانی‌ها.
  - **کتاب‌ها (Book):** فایل‌های PDF و EPUB با جلد گرافیکی.
  - **مقالات (TextWork):** مطالب متنی و PDF پژوهشی.
- 🔍 **جستجوی پیشرفته:** قابلیت جستجو در تمام محتواها (عنوان، توضیحات، دسته‌ها).
- 📂 **دسته‌بندی هوشمند:** سازماندهی محتوا بر اساس موضوع (روانشناسی، درمان، خودیاری، mindfulness و...).
- 🎬 **اسلایدر داینامیک:** نمایش مطالب مهم یا جدید در صفحه اصلی با قابلیت لینک‌دهی.
- 📄 **صفحات داینامیک:**
  - **درباره ما:** اطلاعات دکتر کمان قابل مدیریت از پنل ادمین.
  - **تماس با ما:** فرم تماس که مستقیماً به ادمین ارسال می‌شود.
- 🛡 **امنیت و اعتبارسنجی:**
  - اعتبارسنجی فرمت فایل‌ها (فقط PDF, EPUB, MP3, WAV, JPG, PNG و...).
  - مدیریت خودکار آپلود فایل‌ها در پوشه‌های مشخص.
- 🌐 **واکنش‌گرا (Responsive):** نمایش صحیح در موبایل، تبلت و دسکتاپ.

---

## 📥 نصب و اجرا

### ۱. برای کاربران عادی (وب‌سایت زنده)
*لینک مستقیم به سایت زنده در حال حاضر در دسترس نیست (در حال استقرار روی VPS YTA 2).*

### ۲. برای توسعه‌دهندگان (محیط لوکال)
```bash
# کلون کردن مخزن
git clone https://github.com/Mohammad-Hasan-Kaman/dr-kaman-site.git
cd dr-kaman-site

# ساخت محیط مجازی (اختیاری اما توصیه می‌شود)
python -m venv venv
# در ویندوز:
venv\Scripts\activate
# در لینوکس/مک:
source venv/bin/activate

# نصب وابستگی‌ها
pip install -r requirements.txt

# تنظیم متغیرهای محیطی (اگر .env دارید)
# cp .env.example .env  # اگر فایل نمونه وجود دارد
# و ویرایش .env با تنظیمات دیتابیس و SECRET_KEY

# اجرای مهاجرت‌ها (ایجاد جدول‌های دیتابیس)
python manage.py migrate

# ساخت کاربر ادمین برای ورود به پنل مدیریت
python manage.py createsuperuser

# جمع‌آوری فایل‌های استاتیک
python manage.py collectstatic --noinput

# اجرای سرور توسعه
python manage.py runserver
```
سپس در مرورگر به آدرس `http://127.0.0.1:8000` بروید.

---

## 🛠 تکنولوژی‌های استفاده شده

| تکنولوژی | نقش |
|-----------|-----|
| **Django 4.2+** | فریم‌ورک اصلی وب (MVC Pattern) |
| **Python 3.10+** | زبان برنامه‌نویسی |
| **SQLite** | دیتابیس پیش‌فرض (قابل تغییر به PostgreSQL در پراکشن) |
| **Pillow** | پردازش تصاویر (برای جلد کتاب‌ها و اسلایدرها) |
| **BMitra Font** | فونت فارسیوزی برای نمایش متون |
| **HTML5/CSS3** | اینترفیس سمت کاربر (Template) |

---

## 📸 تصاویری از سایت

*(تصاویر SVG که چیدمان صفحات مختلف را نشان می‌دهند)*

<div align="center">

| صفحه اصلی (Home) | گالری محتوا (Gallery) | جستجو (Search) |
|:---:|:---:|:---:|
| <img src="assets/screenshot_home.svg" width="300" alt="Home Screen"/> | <img src="assets/screenshot_gallery.svg" width="300" alt="Content Gallery"/> | <img src="assets/screenshot_search.svg" width="300" alt="Search Interface"/> |

*افزایش کیفیت تصاویر با کلیک روی آن‌ها*

</div>

---

## 📝 ساختار پروژه

```
dr-kaman-site/
├── assets/                  # فایل‌های گرافیکی و اسکرین‌شات‌ها
│   ├── screenshot_home.svg
│   ├── screenshot_gallery.svg
│   └── screenshot_search.svg
├── audios/                  # اپلیکیشن پادکست‌ها
│   ├── models.py, views.py, urls.py
├── books/                   # اپلیکیشن کتاب‌ها
├── categories/              # دسته‌بندی محتوا
├── core/                    # اپلیکیشن اصلی (اسلایدر، درباره ما، تماس با ما)
├── search/                  # موتور جستجوی سفارشی
├── static/                  # فایل‌های استاتیک (CSS, JS, فونت‌ها)
├── templates/               # فایل‌های HTML
├── CHANGELOG.md             # تاریخچه تغییرات
├── CONTRIBUTING.md          # راهنمای مشارکت
├── LICENSE                  # مجوز MIT
├── README.md                # این فایل
├── requirements.txt         # وابستگی‌های پایتون
└── manage.py                # اسکریپت مدیریت Django
```

---

## 📂 دیتابیس و فایل‌های مدیا

- **دیتابیس:** پیش‌فرض `db.sqlite3`. برای محیط تولید (Production) توصیه می‌شود به **PostgreSQL** تغییر کند.
- **فایل‌های مدیا:** فایل‌های آپلود شده (ویدیو، صدا، کتاب) در پوشه `media/` ذخیره می‌شوند و باید از طریق `MEDIA_URL` و `MEDIA_ROOT` در تنظیمات مدیریت شوند.

---

## 🤝 مشارکت

اگر باگ یا پیشنهادی دارید، لطفاً یک [Issue](https://github.com/Mohammad-Hasan-Kaman/dr-kaman-site/issues) باز کنید.
ورود به پروژه و توسعه آن برای توسعه‌دهندگان خوش‌آمد است. لطفاً از [CONTRIBUTING.md](CONTRIBUTING.md) پیروی کنید.

---

## ⭐ حمایت

اگر از این پروژه استفاده می‌کنید، لطفاً یک **⭐ ستاره** به آن بدهید!
از حمایت شما متشکرم.

[![Star History](https://api.star-history.com/svg?repos=Mohammad-Hasan-Kaman/dr-kaman-site&type=Date)](https://star-history.com/#Mohammad-Hasan-Kaman/dr-kaman-site&Date)

---
*Maintained by Mohammad Hasan Kaman | Last updated: July 2026*

> **سلب مسئولیت:** این پروژه صرفاً برای اهداف آموزشی و آرشیو شخصی طراحی شده است. محتوای سایت متعلق به دکتر محمد رضا کمان می‌باشد.