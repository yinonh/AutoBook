from django.contrib import admin
from review.models import Review

class ReviewAdmin(admin.ModelAdmin):
    search_fields = ['title','text','book__name','adult__user__username']
    list_display = ('title','text')
admin.site.register(Review,ReviewAdmin)

