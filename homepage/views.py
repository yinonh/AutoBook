from django.shortcuts import render
from homepage.models import Event,HomePage

def homepage(request):
    current = HomePage.objects.all()[0]
    events = current.events.order_by('-date')
    return render(request, 'home/home.html',{'home':current, 'events':events})
