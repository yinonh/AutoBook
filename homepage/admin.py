from django.contrib import admin
from homepage.models import Event, HomePage

class EventAdmin(admin.ModelAdmin):
    search_fields = ['id','text','title','registerstudent__user__first_name','registerstudent__user__last_name','registerstudent__user__username','description']
    list_display = ('title','id',)

class HomeAdmin(admin.ModelAdmin):
    search_fields = ['id','title','events__id','events__title','description']
    list_display = ('title','id',)

admin.site.register(Event,EventAdmin)
admin.site.register(HomePage,HomeAdmin)
#Cannot resolve keyword 'text' into field. Choices are: change_Book_date, description, events, id, image, title
