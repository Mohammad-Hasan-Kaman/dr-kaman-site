# -*- coding: utf-8 -*-
"""
تنظیمات مخصوص سرور (پروداکشن)
این فایل فقط برای استقرار روی VPS ساخته شده و از settings.py اصلی ارث‌بری می‌کند.
اجرای سایت روی سرور با این دستور انجام می‌شود:
    python manage.py <cmd> --settings=dr_kaman_site.settings_prod
فایل settings.py اصلی دست‌نخورده باقی مانده است.
"""
from .settings import *  # noqa: F401,F403
import os

DEBUG = False
ALLOWED_HOSTS = ["drkaman.ir", "www.drkaman.ir", "185.235.245.246"]
CSRF_TRUSTED_ORIGINS = ["https://drkaman.ir", "https://www.drkaman.ir", "http://drkaman.ir", "http://www.drkaman.ir"]

# تنظیمات پروکسی معکوس (nginx با HTTPS روی دروازه)
USE_X_FORWARDED_HOST = True
SECURE_PROXY_SSL_HEADER = ("HTTP_X_FORWARDED_PROTO", "https")

# کوکی‌های امن (فعال چون ترافیک از HTTPS می‌آید)
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True

# اندازه آپلود بزرگ (ویدیوها می‌تونن سنگین باشن)
DATA_UPLOAD_MAX_MEMORY_SIZE = 104857600  # 100 MB
FILE_UPLOAD_MAX_MEMORY_SIZE = 104857600   # 100 MB

# کلید امنیتی از محیط خوانده می‌شود — هرگز کلید واقعی را در گیت کامیت نکنید.
# روی سرور: export DJANGO_SECRET_KEY='...'‎ (یا در systemd unit / فایل .env که gunicorn می‌خواند)
SECRET_KEY = os.environ.get("DJANGO_SECRET_KEY", "")
if not SECRET_KEY or len(SECRET_KEY) < 50 or "insecure" in SECRET_KEY:
    raise RuntimeError(
        "DJANGO_SECRET_KEY missing/weak — generate one with: "
        'python -c "import secrets; print(secrets.token_urlsafe(64))"')
