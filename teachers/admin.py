from django.contrib import admin
from teachers.models import Teacher

class TeacherAdmin(admin.ModelAdmin):
    search_fields = ['HourRate','LessonMethod','Teacher_Name','title']
    list_display = ('Teacher_Name','title','LessonMethod','HourRate')

admin.site.register(Teacher,TeacherAdmin)
# Register your models here.
