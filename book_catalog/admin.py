from django.contrib import admin
from book_catalog.models import Book


class BookAdmin(admin.ModelAdmin):
    search_fields = ['name','author_name','key_words','genre','Grade',]
    list_display = ('name','author_name','genre','Grade','key_words',)

admin.site.register(Book, BookAdmin)