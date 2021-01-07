from django.contrib import admin
from Forum.models import Forum,Comments


class ForumAdmin(admin.ModelAdmin):
    search_fields = ['title','student__user__username',]
    list_display = ('title',)

class CommentsAdmin(admin.ModelAdmin):
    search_fields = ['title', 'student__user__username','forum__title' ]
    list_display = ('title',)

admin.site.register(Forum,ForumAdmin)
admin.site.register(Comments,CommentsAdmin)

# Register your models here.
