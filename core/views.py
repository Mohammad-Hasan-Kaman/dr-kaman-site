# dr_kaman_site/core/views.py

from django.shortcuts import render
from texts.models import TextWork
from audios.models import AudioWork
from videos.models import VideoWork
from .models import Slider
from categories.models import Category


def home(request):
    """
    این ویو، داده‌های لازم برای صفحه اصلی جامع را به صورت امن و کامل آماده می‌کند.
    """
    # اسلایدر: فقط اسلایدهای فعال را از مدل جدید می‌خوانیم
    slider_images = Slider.objects.filter(is_active=True)

    # آخرین آثار
    latest_texts = TextWork.objects.order_by('-created_at')[:3]
    latest_audios = AudioWork.objects.order_by('-created_at')[:3]
    latest_videos = VideoWork.objects.order_by('-created_at')[:3]

    # دسته‌بندی‌ها برای نمایش
    featured_categories = Category.objects.all()[:4]

    context = {
        'slider_images': slider_images,
        'latest_texts': latest_texts,
        'latest_audios': latest_audios,
        'latest_videos': latest_videos,
        'featured_categories': featured_categories,
    }
    return render(request, 'core/home.html', context)


def about(request):
    return render(request, 'core/about.html')


def contact(request):
    return render(request, 'core/contact.html')