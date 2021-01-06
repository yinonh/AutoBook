from django.shortcuts import render
from Activite_stud.models import Activity

# Create your views here.
def Activity_stud(request):
    activities = Activity.objects.all()
    return  rander (request,'Activite_stud/Activity_stud.html',{'activities':activities})