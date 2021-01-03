from django.shortcuts import render, get_object_or_404,redirect
from book_catalog.models import Book
from homepage.models import Event

def meadult(request):
    return render(request, 'mepage/adult/mepageadult.html')

def meadultfavourites(request):
    return render(request, 'mepage/adult/favouritebooks.html')

def meAdultPossesses(request):
    possessBooks = request.user.adult.Adultposses.all()
    return render(request, 'mepage/adult/possessedbooks.html',{"possessBooks":possessBooks})

def mestudent(request):
    return render(request, 'mepage/student/mepagestudent.html')

def mestudentpossesses(request):
    possessBooks = request.user.student.Studentposses.all()
    return render(request, 'mepage/adult/possessedbooks.html', {"possessBooks": possessBooks})

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
    books = Book.objects.filter(posses=True)
    books = list(filter(lambda x:not x.takenout,books))
    return render(request, 'mepage/admin/getout.html',{'books':books})
