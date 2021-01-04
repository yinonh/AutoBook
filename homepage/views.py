from django.shortcuts import render
from homepage.models import Event,HomePage
from book_catalog.models import Book

def homepage(request):
    try:
        current = HomePage.objects.all()[0]
        events = current.events.order_by('-date')
        return render(request, 'home/home.html',{'home':current, 'events':events})
    except:
        books = Book.objects.all()
        return render(request,"book_cataloge/bookcataloge.html",{"books" : books})
