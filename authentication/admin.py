from django.contrib import admin
from .models import Student,Adult

class AdultAdmin(admin.ModelAdmin):
    search_fields = ['ID_Number','id',]
    list_display = ('user',)


admin.site.register(Adult,AdultAdmin)
admin.site.register(Student)
