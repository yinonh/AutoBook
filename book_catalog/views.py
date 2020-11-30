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

