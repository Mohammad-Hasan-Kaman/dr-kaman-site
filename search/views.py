from django.shortcuts import render
from texts.models import TextWork
from audios.models import AudioWork
from videos.models import VideoWork
from django.db.models import Q


def search_results(request):
    query = request.GET.get('q', '')

    text_results = TextWork.objects.none()
    audio_results = AudioWork.objects.none()
    video_results = VideoWork.objects.none()

    if query:
        text_results = TextWork.objects.filter(Q(title__icontains=query) | Q(description__icontains=query)).distinct()
        audio_results = AudioWork.objects.filter(Q(title__icontains=query) | Q(description__icontains=query)).distinct()
        video_results = VideoWork.objects.filter(Q(title__icontains=query) | Q(description__icontains=query)).distinct()

    has_results = text_results.exists() or audio_results.exists() or video_results.exists()

    context = {
        'query': query,
        'text_results': text_results,
        'audio_results': audio_results,
        'video_results': video_results,
        'has_results': has_results
    }
    return render(request, 'search/results.html', context)