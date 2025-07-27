from django.shortcuts import render
from .models import VideoWork, Category
from django.db.models import Q

def video_list(request):
    search_query = request.GET.get('q', '')
    category_id = request.GET.get('category', '')
    videos = VideoWork.objects.all().order_by('-created_at')
    if search_query:
        videos = videos.filter(Q(title__icontains=search_query) | Q(description__icontains=search_query))
    if category_id:
        videos = videos.filter(category_id=category_id)
    all_categories = Category.objects.all()
    context = {
        'videos': videos,
        'categories': all_categories,
        'selected_category_id': int(category_id) if category_id.isdigit() else None,
        'search_query': search_query,
    }
    return render(request, 'videos/list.html', context)