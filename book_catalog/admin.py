from django.contrib import admin
from book_catalog.models import Book


class BookAdmin(admin.ModelAdmin):
    search_fields = ['name',]
    list_display = ('name',)

admin.site.register(Book, BookAdmin)