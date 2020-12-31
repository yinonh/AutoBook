from django.shortcuts import render, get_object_or_404,redirect
from .models import Book
from django.contrib.auth.decorators import login_required
from django.core.exceptions import ObjectDoesNotExist


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
    elif request.GET.get("AuthorName"):
        books = list(filter(lambda x: request.GET.get('AuthorName').lower() in x.author_name.lower(), books))
    elif request.GET.get("Name"):
        books = list(filter(lambda x: request.GET.get('Name').lower() in x.name.lower(), books))
    if request.GET.get("Available"):
        books = list(filter(lambda x: x.available == True, books))
    else:
        books = list(filter(lambda x: x.available == False, books))
    if request.GET.get("Study_Book"):
        books = list(filter(lambda x: x.study_book == True, books))
    else:
        books = list(filter(lambda x: x.study_book == False, books))
    if books == []:
        books = -1

    return render(request, 'book_cataloge/filteredbooks.html',{'books':books})

def book_card(request, book_id):
    book = get_object_or_404(Book, pk=book_id)
    if request.method == "POST":
        if not request.user.is_authenticated:
            return redirect("loginU")
        try:
            request.user.adult.Adultposses.add(book)
            request.user.adult.save()
            book.posses = True
            book.save()
        except ObjectDoesNotExist:
            request.user.student.Studentposses.add(book)
            request.user.student.save()
            book.posses = True
            book.save()

    return render(request,'book_cataloge/book_card.html',{'book':book})



