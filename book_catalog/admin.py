from django.contrib import admin
from book_catalog.models import Book,AudioBook


class BookAdmin(admin.ModelAdmin):
    search_fields = ['name','author_name','key_words','genre','Grade',]
    list_display = ('name','author_name','genre','Grade','key_words',)

class AudioBookAdmin(admin.ModelAdmin):
    search_fields = ['name', 'key_words', 'genre']
    list_display = ('name', 'genre', 'key_words',)

admin.site.register(Book, BookAdmin)
admin.site.register(AudioBook, AudioBookAdmin)