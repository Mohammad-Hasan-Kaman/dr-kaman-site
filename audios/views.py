from django.shortcuts import render
from .models import AudioWork, Category
from django.db.models import Q

def audio_list(request):
    search_query = request.GET.get('q', '')
    category_id = request.GET.get('category', '')
    audios = AudioWork.objects.all().order_by('-created_at')

    if search_query:
        audios = audios.filter(Q(title__icontains=search_query) | Q(description__icontains=search_query))
    if category_id:
        audios = audios.filter(category_id=category_id)

    all_categories = Category.objects.all()
    context = {
        'audios': audios,
        'categories': all_categories,
        'selected_category_id': int(category_id) if category_id.isdigit() else None,
        'search_query': search_query,
    }
    return render(request, 'audios/list.html', context)