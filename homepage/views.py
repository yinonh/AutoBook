from django.shortcuts import render
from homepage.models import Event

def homepage(request):
    events = Event.objects.all()
    return render(request, 'home/home.html',{'events':events})
