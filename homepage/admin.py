from django.contrib import admin
from homepage.models import Event, HomePage

class EventAdmin(admin.ModelAdmin):
    search_fields = ['id','text','title','registerstudent__user__first_name','registerstudent__user__last_name','registerstudent__user__username',]
    list_display = ('title','id','date')

class HomeAdmin(admin.ModelAdmin):
    search_fields = ['id','title','events__id','events__title','description']
    list_display = ('title','id','change_Book_date')

admin.site.register(Event,EventAdmin)
admin.site.register(HomePage,HomeAdmin)
