from django.shortcuts import render, get_object_or_404,redirect
from .models import Book
from authentication.models import Adult
from django.contrib.auth.decorators import login_required
from django.core.exceptions import ObjectDoesNotExist
from review.models import Review
import datetime




def home(request):
    return render(request, 'home/home.html')

def simple (request):
    return render(request, 'home/simple.html')

def bookcataloge (request):
    try:
        if request.user.adult:
            books = list(Book.objects.filter(study_book=False,kids=False))[:6]

    except:
        try:
            if request.user.student:
                books = list(Book.objects.filter(adult_only=False))[:6]
        except:
            books = list(Book.objects.all())[:4]


    return render(request,'book_cataloge/bookcataloge.html',{'books': books})

def contact(request):
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
    if request.GET.get("grade") != None:
        books = list(filter(lambda x: str(x.Grade) == str(request.GET.get("grade")), books))
    if books == []:
        books = -1

    return render(request, 'book_cataloge/filteredbooks.html',{'books':books})

def book_card(request, book_id):
    book = get_object_or_404(Book, pk=book_id)
    reviews = Review.objects.filter(book= book)
    rank, count = 0, 0
    countbooks = 0
    for reviw in reviews:
        rank += reviw.rank
        count += 1
    try:
        for book1 in request.user.student.Studentposses.all():
            if book1.study_book == False:
                countbooks += 1
    except:
        pass
    if request.method == "POST":
        if "favourite" in request.POST:
            request.user.adult.FavouriteBooks.add(book)
            request.user.adult.save()
        elif "notFavourite" in request.POST:
            request.user.adult.FavouriteBooks.remove(book)
            request.user.adult.save()
        elif "posses" in request.POST:
            if not request.user.is_authenticated:
                return redirect("loginU")
            try:
                request.user.adult.Adultposses.add(book)
                request.user.adult.save()
                book.posses = True
                book.Take_Date=datetime.datetime.now()
                book.save()
            except ObjectDoesNotExist:
                request.user.student.Studentposses.add(book)
                request.user.student.save()
                book.posses = True
                book.Take_Date = datetime.datetime.now()
                book.save()
    suggestions = []
    try:
        bookPosses = request.user.adult.Adultposses.count()
        for adult in Adult.objects.all():
            if len(suggestions) >= 3:
                break
            if adult != request.user.adult:
                if book in adult.FavouriteBooks.all():
                    for item in adult.FavouriteBooks.all():
                        if item != book and item.genre == book.genre:
                            suggestions.append(item)
        suggestions = suggestions[:3]
        suggestions = set(suggestions)
    except:
        try:
            bookPosses = request.user.student.Studentposses.count()
        except:
            bookPosses=0
    rank = rank//count if count > 0 else 0



    return render(request, 'book_cataloge/book_card.html', {'book': book, 'suggestions': suggestions, 'rank': range(rank),"empty":range(5 - rank),"bookPosses": bookPosses,'countbooks':countbooks})


def bookPage(request, page_num):
    if (page_num < 1):
        return redirect("bookcataloge")
    try:
        if request.user.adult:
            books = list(Book.objects.filter(study_book=False,kids=False))[6*page_num:6*page_num+6]
    except:
        try:
            if request.user.student:
                books = list(Book.objects.filter(adult_only=False))[6*page_num:6*page_num+6]
        except:
            books = list(Book.objects.all())[6*page_num:6*page_num+6]
    if len(list(Book.objects.all())[6*(page_num+1):6*(page_num+1)+6]) < 1:
        return render(request, "book_cataloge/bookPages.html", {"books": books, "plus": page_num, "minus": page_num-1,"last": True})

    return render(request, "book_cataloge/bookPages.html",{"books": books, "plus": page_num + 1, "minus": page_num - 1, "last": False})


