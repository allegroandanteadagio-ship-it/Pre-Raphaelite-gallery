from django.shortcuts import render
from .models import Artwork, Artist
from django.db.models import Q

# 1. ГЛАВНАЯ СТРАНИЦА
def home(request):
    return render(request, 'home.html')

# 2. СТРАНИЦА ХУДОЖНИКОВ
def artist_list(request):
    artists = Artist.objects.all()
    return render(request, 'artists.html', {'artists': artists})

# 3. СТРАНИЦА КАРТИН С ПОИСКОМ
def artwork_list(request):
    # Получаем поисковый запрос
    search_query = request.GET.get('q', '')
    
    # Все картины
    artworks = Artwork.objects.all()
    
    # Если есть поисковый запрос
    if search_query:
        artworks = artworks.filter(
            Q(title__icontains=search_query) |
            Q(artist__name__icontains=search_query)
        ).distinct()
    
    return render(request, 'artworks.html', {
        'artworks': artworks,
        'search_query': search_query,
    })