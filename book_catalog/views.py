from django.shortcuts import render
from .models import Book

books = Book.objects.all()
def home(request):
    return render(request, 'home/home.html')

def simple (request):
    return render(request, 'home/simple.html')

def bookcataloge (request):
    return render(request,'book_cataloge/bookcataloge.html',{'books': books})

def contact (request):
    return render(request,'contact/contact.html')

def filteredbooks (request):
    books = Book.objects.all()
    if request.GET.get('genre')!='All':
        books = list(filter(lambda x:x.genre == request.GET.get('genre'), books))
    if request.GET.get("AuthorName"):
        books = list(filter(lambda x: x.author_name.lower() == request.GET.get('AuthorName').lower(), books))
    if request.GET.get("Name"):
        books = list(filter(lambda x: x.name.lower() == request.GET.get('Name').lower(), books))
    if request.GET.get("Available"):
        books = list(filter(lambda x: x.available == True, books))
    else:
        books = list(filter(lambda x: x.available == False, books))

    return render(request, 'book_cataloge/filteredbooks.html',{'books':books})



