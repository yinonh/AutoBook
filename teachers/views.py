from django.shortcuts import render
from teachers.models import Teacher



def teachers(request):
    teachers1=Teacher.objects.all()
    return render(request,'teachers/teachers.html',{'teachers':teachers1})