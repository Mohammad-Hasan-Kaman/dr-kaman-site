from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from core import seo_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('texts/', include('texts.urls')),
    path('audios/', include('audios.urls')),
    path('videos/', include('videos.urls')),
    path('search/', include('search.urls')),
    path('books/', include('books.urls')),  # <-- این خط را اضافه کنید

    # --- SEO: robots.txt، sitemap.xml، llms.txt ---
    path('robots.txt', seo_views.robots_txt, name='robots_txt'),
    path('sitemap.xml', seo_views.sitemap_xml, name='sitemap_xml'),
    path('llms.txt', seo_views.llms_txt, name='llms_txt'),

    path('', include('core.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)