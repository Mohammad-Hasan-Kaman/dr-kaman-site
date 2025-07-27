from django.shortcuts import render
from .models import TextWork, Category
from django.db.models import Q

def text_list(request):
    search_query = request.GET.get('q', '')
    category_id = request.GET.get('category', '')
    texts = TextWork.objects.all().order_by('-created_at')
    if search_query:
        texts = texts.filter(Q(title__icontains=search_query) | Q(description__icontains=search_query))
    if category_id:
        texts = texts.filter(category_id=category_id)
    all_categories = Category.objects.all()
    context = {
        'texts': texts,
        'categories': all_categories,
        'selected_category_id': int(category_id) if category_id.isdigit() else None,
        'search_query': search_query,
    }
    return render(request, 'texts/list.html', context)