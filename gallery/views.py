from django.shortcuts import render
from .models import Artist, Artwork

def home(request):
    total_artists = Artist.objects.count()
    total_artworks = Artwork.objects.count()
    return render(request, 'home.html', {
        'total_artists': total_artists,
        'total_artworks': total_artworks,
    })

def artist_list(request):  # БЫЛО artists_list → СТАЛО artist_list
    artists = Artist.objects.all().order_by('name')
    return render(request, 'artists.html', {'artists': artists})

def artwork_list(request):  # БЫЛО artworks_list → СТАЛО artwork_list
    artworks = Artwork.objects.all().select_related('artist').order_by('title')
    return render(request, 'artworks.html', {'artworks': artworks})