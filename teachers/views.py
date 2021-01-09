from django.shortcuts import render
from teachers.models import Teacher
from django.shortcuts import render, get_object_or_404,redirect
from django.contrib.auth.decorators import login_required



@login_required
def teachers(request):
    teachers1=Teacher.objects.all()
    teachers1 =teachers1.order_by('-Teacher_date')
    return render(request,'teachers/teachers.html',{'teachers':teachers1})
@login_required
def teachercard(request,teacher_id):
    teacher = get_object_or_404(Teacher, pk=teacher_id)
    return render(request,'teachers/teachercard.html',{'teacher':teacher})