from django.shortcuts import render, get_object_or_404, redirect
from book_catalog.models import Book
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist
from authentication.models import Student,Adult
from homepage.models import Event


def meadult(request):
    return render(request, 'mepage/adult/mepageadult.html')

def meadultfavourites(request):
    return render(request, 'mepage/adult/favouritebooks.html')

def meAdultPossesses(request):
    possessBooks = request.user.adult.Adultposses.all()
    return render(request, 'mepage/adult/possessedbooks.html',{"possessBooks":possessBooks})

def meAdultReturn(request, book_id):
    book = get_object_or_404(Book, pk=book_id)
    if request.method == "POST":
        if 'yes' in request.POST:
            book.takenout=True
            book.returned=False
            book.save()
            return redirect("meadultpossesses")
        elif 'no' in request.POST:
            return redirect("meadultpossesses")
        elif 'cancelrequest' in request.POST:
            for user1 in Adult.objects.all():
                if book in user1.Adultposses.all():
                    user1.Adultposses.remove(book)
                    user1.save()
                    book.posses = False
                    book.save()
            return redirect("meadultpossesses")
        elif 'cancelreturn' in request.POST:
            book.takenout = True
            book.returned = True
            book.save()
            return redirect("meadultpossesses")

    return render(request, 'mepage/adult/meAdultReturn.html',{"book":book})

def meAdultDamage(request, book_id):
    book = get_object_or_404(Book, pk=book_id)
    if request.method == "POST":
        if 'yes' in request.POST:
            damagedes = request.POST.get('damagetext')
            book.Is_Damaged=True
            book.Damage_Description=damagedes
            print(book.Damage_Description)
            book.save()
            return redirect("meadultpossesses")
        elif 'no' in request.POST:
            return redirect("meadultpossesses")
    return render(request, 'mepage/adult/meAdultDamage.html',{"book":book})

def meStudentDamage(request, book_id):
    book = get_object_or_404(Book, pk=book_id)
    if request.method == "POST":
        if 'yes' in request.POST:
            damagedes = request.POST.get('damagetext')
            book.Is_Damaged=True
            book.Damage_Description=damagedes
            print(book.Damage_Description)
            book.save()
            return redirect("mestudentpossesses")
        elif 'no' in request.POST:
            return redirect("mestudentpossesses")
    return render(request, 'mepage/student/meStudentDamage.html',{"book":book})
def meStudentReturn(request, book_id):
    book = get_object_or_404(Book, pk=book_id)
    if request.method == "POST":
        if 'yes' in request.POST:
            book.takenout = True
            book.returned = False
            book.save()
            return redirect("mestudentpossesses")
        elif 'no' in request.POST:
            return redirect("mestudentpossesses")
        elif 'cancelrequest' in request.POST:
            for user1 in Student.objects.all():
                if book in user1.Studentposses.all():
                    user1.Studentposses.remove(book)
                    user1.save()
                    book.posses = False
                    book.save()
            return redirect("mestudentpossesses")
        elif 'cancelreturn' in request.POST:
            book.takenout = True
            book.returned = True
            book.save()
            return redirect("mestudentpossesses")

    return render(request, 'mepage/student/meStudentReturn.html', {"book": book})

def mestudent(request):
    return render(request, 'mepage/student/mepagestudent.html')

def mestudentpossesses(request):
    possessBooks = request.user.student.Studentposses.all()
    return render(request, 'mepage/student/possessedbooks.html', {"possessBooks": possessBooks})

def mestudentevents(request):
    events = Event.objects.all()
    return render(request, 'mepage/student/events.html',{"events":events})

def registerEvents(request, event_id):
    event = get_object_or_404(Event, pk=event_id)
    if request.method == "POST":
        if "cancelled" in request.POST:
            event.registerstudent.remove(request.user.student)
        elif "register" in request.POST:
            event.registerstudent.add(request.user.student)

        event.save()
        return redirect("mestudentevents")

    return render(request, 'mepage/student/registerEvent.html', {"event": event})

def mestudentlendedbooks(request):
    return render(request, 'mepage/student/lendedbooks.html')

def meadminpage(request):
    return render(request, 'mepage/admin/reports.html')

def getout(request):
    if request.method == 'POST':
        id_list = request.POST.getlist('book.id')
        for bookid in id_list:
            book = get_object_or_404(Book, pk=bookid)
            book.takenout=True
            book.save()
        cancelid_list = request.POST.getlist('cancelbook.id')
        for bookid in id_list:
            book = get_object_or_404(Book, pk=bookid)
            book.takenout = True
            book.save()
        for cancelid in cancelid_list:
            book = get_object_or_404(Book, pk=cancelid)
            for user1 in Student.objects.all():
                if book in user1.Studentposses.all():
                    user1.Studentposses.remove(book)
                    user1.save()
                    book.posses = False
                    book.save()
            for user1 in Adult.objects.all():
                if book in user1.Adultposses.all():
                    user1.Adultposses.remove(book)
                    user1.save()
                    book.posses = False
                    book.save()
    books = Book.objects.filter(posses=True,takenout=False)
    books = list(filter(lambda x:not x.takenout,books))
    return render(request, 'mepage/admin/getout.html',{'books':books})

def getin(request):
    if request.method == 'POST':
        id_list = request.POST.getlist('book.id')
        for id1 in id_list:
            book = get_object_or_404(Book, pk=id1)
            for user1 in Student.objects.all():
                if book in user1.Studentposses.all():
                    user1.Studentposses.remove(book)
                    user1.save()
                    book.takenout = False
                    book.returned = True
                    book.posses = False
                    book.save()
            for user1 in Adult.objects.all():
                if book in user1.Adultposses.all():
                    user1.Adultposses.remove(book)
                    user1.save()
                    book.takenout = False
                    book.returned = True
                    book.posses = False
                    book.save()
    books = Book.objects.filter(returned=False)
    books = list(filter(lambda x:not x.returned,books))
    return render(request, 'mepage/admin/getin.html',{'books':books})

def damaged (request):
    if request.method == 'POST':
        id_list = request.POST.getlist('book.id')
        for bookid in id_list:
            book = get_object_or_404(Book, pk=bookid)
            book.Is_Damaged=False
            book.Damage_Description=None
            book.save()
    books = Book.objects.filter(Is_Damaged=True)
    return render(request, 'mepage/admin/damaged.html',{'books':books})

