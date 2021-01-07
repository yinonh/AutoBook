from django.contrib import admin
from .models import Student,Adult

class AdultAdmin(admin.ModelAdmin):
    search_fields = ['user__first_name', 'user__last_name','ID_Number' ,'id','user__username',]
    list_display = ('user','id','ID_Number')

class StudentAdmin(admin.ModelAdmin):
    search_fields = ['user__first_name','user__last_name','id','grade','user__username',]
    list_display = ('user','id','grade')


admin.site.register(Adult,AdultAdmin)
admin.site.register(Student,StudentAdmin)
