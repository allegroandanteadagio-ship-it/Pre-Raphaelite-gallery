from django.contrib import admin
from .models import Artist, Artwork

@admin.register(Artist)
class ArtistAdmin(admin.ModelAdmin):
    list_display = ('name', 'birth_year', 'death_year', 'country')
    search_fields = ('name', 'biography')
    list_filter = ('country',)

@admin.register(Artwork)
class ArtworkAdmin(admin.ModelAdmin):
    list_display = ('title', 'artist', 'year', 'technique', 'location')
    list_filter = ('year', 'artist', 'technique')
    search_fields = ('title', 'description')