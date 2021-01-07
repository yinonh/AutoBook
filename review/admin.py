from django.contrib import admin
from review.models import Review

class ReviewAdmin(admin.ModelAdmin):
    search_fields = ['title','text','book__name']
    list_display = ('title',)

admin.site.register(Review,ReviewAdmin)

# Cannot resolve keyword 'user' into field. Choices are: adult, book, id, rank, text, title
