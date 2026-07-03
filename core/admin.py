from django.contrib import admin
from .models import Slider, AboutPage, ContactPage


@admin.register(Slider)
class SliderAdmin(admin.ModelAdmin):
    list_display = ('title', 'is_active', 'link')
    list_filter = ('is_active',)
    search_fields = ('title', 'description')


@admin.register(AboutPage)
class AboutPageAdmin(admin.ModelAdmin):
    list_display = ('title', 'updated_at')
    readonly_fields = ('updated_at',)


@admin.register(ContactPage)
class ContactPageAdmin(admin.ModelAdmin):
    list_display = ('title', 'updated_at', 'phone', 'email')
    readonly_fields = ('updated_at',)