from django.shortcuts import render
from teachers.models import Teacher
from django.shortcuts import render, get_object_or_404,redirect



def teachers(request):
    teachers1=Teacher.objects.all()
    return render(request,'teachers/teachers.html',{'teachers':teachers1})
def teachercard(request,teacher_id):
    teacher = get_object_or_404(Teacher, pk=teacher_id)
    return render(request,'teachers/teachercard.html',{'teacher':teacher})