from django.shortcuts import render

def text_list(request):
    """صفحه آثار متنی در حال آماده‌سازی"""
    context = {
        'message': 'این بخش در حال آماده‌سازی است. به زودی آثار متنی دکتر کمن در اینجا قابل دسترسی خواهد بود.',
    }
    return render(request, 'texts/preparation.html', context)