from django.shortcuts import render
from audios.models import AudioWork
from videos.models import VideoWork
from books.models import Book
from .models import Slider
from categories.models import Category
from .models import Slider, AboutPage, ContactPage

def home(request):
    """
    این ویو، داده‌های لازم برای صفحه اصلی جامع را به صورت امن و کامل آماده می‌کند.
    """
    # اسلایدر: فقط اسلایدهای فعال را از مدل جدید می‌خوانیم
    slider_images = Slider.objects.filter(is_active=True)

    # آخرین آثار
    latest_audios = AudioWork.objects.order_by('-created_at')[:3]
    latest_videos = VideoWork.objects.order_by('-created_at')[:3]
    latest_books = Book.objects.order_by('-created_at')[:3]

    # دسته‌بندی‌ها برای نمایش
    featured_categories = Category.objects.all()[:4]

    context = {
        'slider_images': slider_images,
        'latest_audios': latest_audios,
        'latest_videos': latest_videos,
        'latest_books': latest_books,
        'featured_categories': featured_categories,
    }
    return render(request, 'core/home.html', context)


def about(request):
    # دریافت محتوای داینامیک صفحه درباره
    about_page = AboutPage.objects.first()
    if not about_page:
        about_page = AboutPage.objects.create(
            content="در حال حاضر محتوای صفحه درباره در حال تکمیل است."
        )
    return render(request, 'core/about.html', {'about_page': about_page})


def contact(request):
    # دریافت محتوای داینامیک صفحه تماس
    contact_page = ContactPage.objects.first()
    if not contact_page:
        contact_page = ContactPage.objects.create(
            content="در حال حاضر اطلاعات تماس در حال تکمیل است.",
            phone="",
            email="",
            address=""
        )
    return render(request, 'core/contact.html', {'contact_page': contact_page})