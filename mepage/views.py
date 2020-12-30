from django.shortcuts import render, get_object_or_404,redirect
from book_catalog.models import Book

def meadult(request):
    return render(request, 'mepage/adult/mepageadult.html')

def meadultfavourites(request):
    return render(request, 'mepage/adult/favouritebooks.html')

def meadultpossesses(request):
    return render(request, 'mepage/adult/possessedbooks.html')

def mestudent(request):
    return render(request, 'mepage/student/mepagestudent.html')

def mestudentpossesses(request):
    return render(request, 'mepage/student/possessedbooks.html')

def mestudentevents(request):
    return render(request, 'mepage/student/events.html')

def mestudentlendedbooks(request):
    return render(request, 'mepage/student/lendedbooks.html')

def meadminpage(request):
    return render(request, 'mepage/admin/reports.html')

def getout(request):
    books = Book.objects.filter(posses=True)
    books = list(filter(lambda x:not x.takenout,books))
    return render(request, 'mepage/admin/getout.html',{'books':books})
