from django.contrib import admin

from .models import Movie


@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    list_display = ('title', 'genre', 'release_year', 'director', 'rating', 'is_series')
    list_filter = ('genre', 'is_series', 'release_year')
    search_fields = ('title', 'director')