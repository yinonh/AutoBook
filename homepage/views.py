from django.shortcuts import render
from homepage.models import Event,HomePage
from book_catalog.models import Book
from django.shortcuts import render, get_object_or_404,redirect


def homepage(request):
    try:
        current = HomePage.objects.all()[0]
        events = current.events.order_by('-date')
        return render(request, 'home/home.html',{'home':current, 'events':events})
    except:
        books = Book.objects.all()
        return render(request,"book_cataloge/bookcataloge.html",{"books" : books})

def searchresults(request):
    if request.method=='POST':
        books = Book.objects.all()
        events=Event.objects.all()
        result=[]
        eventres=[]
        query=request.POST.get('query')
        for book in books:
            if query.lower() in book.author_name.lower():
                result.append(book)
        for book in books:
            if query.lower() in book.name.lower():
                result.append(book)
        for event in events:
            if query.lower() in event.title.lower():
                eventres.append(event)
        result=set(result)
    return render(request, "search/results.html",{'query':query,'books':result,'events':eventres})
