# books/views.py

from django.shortcuts import render
from .models import Book
from django.db.models import Q


def book_list(request):
    search_query = request.GET.get('q', '')

    books = Book.objects.all().order_by('-created_at')

    if search_query:
        books = books.filter(Q(title__icontains=search_query) | Q(description__icontains=search_query))

    context = {
        'books': books,
        'search_query': search_query,
    }
    return render(request, 'books/list.html', context)