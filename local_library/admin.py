from django.contrib import admin
from .models import Author, Genre, Book


class BookAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'author', 'display_genre')
    list_display_links = ('id', 'title')
    search_fields = ('title', 'summary')
    list_per_page = 10
    list_filter = ('author', )


admin.site.register(Book, BookAdmin)
admin.site.register(Author)
admin.site.register(Genre)
