# core/seo_views.py
"""
ویوهای SEO: robots.txt، sitemap.xml و llms.txt
این فایل جداگانه است تا نیازی به تغییر urls.py اصلی نباشد.
"""
from django.http import HttpResponse
from django.template.loader import render_to_string


def robots_txt(request):
    """robots.txt — راهنمایی موتورهای جستجو و خزنده‌های هوش مصنوعی."""
    content = """User-agent: *
Allow: /

# Sitemap
Sitemap: https://drkaman.ir/sitemap.xml

# اجازه صریح به خزنده‌های هوش مصنوعی (LLMs)
User-agent: GPTBot
Allow: /

User-agent: ChatGPT-User
Allow: /

User-agent: CCBot
Allow: /

User-agent: anthropic-ai
Allow: /

User-agent: ClaudeBot
Allow: /

User-agent: Google-Extended
Allow: /

User-agent: PerplexityBot
Allow: /

User-agent: Applebot-Extended
Allow: /
"""
    return HttpResponse(content, content_type="text/plain; charset=utf-8")


def sitemap_xml(request):
    """sitemap.xml — فهرست صفحات برای گوگل."""
    from videos.models import VideoWork
    from audios.models import AudioWork
    from books.models import Book
    from texts.models import TextWork

    context = {
        'videos': VideoWork.objects.order_by('-created_at')[:100],
        'audios': AudioWork.objects.order_by('-created_at')[:100],
        'books': Book.objects.order_by('-created_at')[:100],
        'texts': TextWork.objects.order_by('-created_at')[:100],
    }
    xml = render_to_string('core/sitemap.xml', context)
    return HttpResponse(xml, content_type="application/xml; charset=utf-8")


def llms_txt(request):
    """llms.txt — معرفی سایت برای مدل‌های زبانی (استاندارد llmstxt.org)."""
    content = """# دکتر محمد رضا کمن

> روانشناس بالینی، مشاور خانواده، نویسنده و پژوهشگر ایرانی.
> مجموعه‌ای از آثار علمی، کتاب‌ها، ویدیوها، فایل‌های صوتی و متون آموزشی در حوزه روانشناسی.

## درباره
- [درباره دکتر کمن](https://drkaman.ir/about/): معرفی، سوابق علمی و حرفه‌ای.
- [تماس](https://drkaman.ir/contact/): راه‌های ارتباطی.

## بخش‌ها
- [آثار تصویری](https://drkaman.ir/videos/): ویدیوهای آموزشی روانشناسی.
- [آثار صوتی](https://drkaman.ir/audios/): پادکست‌ها و فایل‌های صوتی آموزشی.
- [کتاب‌ها](https://drkaman.ir/books/): تألیفات دکتر کمن با امکان دانلود بخشی از کتاب و خرید نسخه فیزیکی.
- [آثار متنی](https://drkaman.ir/texts/): مقالات و متون علمی.
- [جستجو](https://drkaman.ir/search/): جستجو در تمام آثار.

## نحوه استناد
- صاحب اثر: دکتر محمد رضا کمن
- وب‌سایت رسمی: https://drkaman.ir/
- زبان محتوا: فارسی (fa)
"""
    return HttpResponse(content, content_type="text/plain; charset=utf-8")
