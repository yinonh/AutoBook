from django.shortcuts import render, get_object_or_404, redirect
from book_catalog.models import Book,AudioBook
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist
from authentication.models import Student,Adult
from homepage.models import Event,HomePage
from django.http import HttpResponse
from authentication.forms import AdultProfileForm,UserCreationForm,ExtendedUserCreationForm
import datetime
from django.contrib.auth.decorators import login_required,user_passes_test

def is_student(user):
    try:
        return user.is_authenticated and user.student is not None
    except Student.DoesNotExist:
        return False

def is_adult(user):
    try:
        return user.is_authenticated and user.adult is not None
    except Adult.DoesNotExist:
        return False

def is_admin(user):
    try:
        return user.is_authenticated and user.is_superuser
    except User.DoesNotExist:
        return False



@user_passes_test(is_adult)
def meadult(request):
    if request.method == 'GET':
        form1 = ExtendedUserCreationForm(instance=request.user)
        form2 = AdultProfileForm(instance=request.user.adult)
        return render(request, 'mepage/adult/mepageadult.html', {'form1': form1})
    if request.method == 'POST':
        try:
            form1 = ExtendedUserCreationForm(request.POST,instance=request.user)
            form1.save()
            return redirect('homepage')
        except ValueError:
            return render(request,'mepage/adult/mepageadult.html',{'form1': form1,'error':'Invalid Username Or Password Please Try Again'})


# # @login_required
# def meadultfavourites(request):
#     return render(request, 'mepage/adult/favouritebooks.html')

@login_required
def meAdultPossesses(request):
    possessBooks = request.user.adult.Adultposses.all()
    return render(request, 'mepage/adult/possessedbooks.html',{"possessBooks":possessBooks})



@user_passes_test(is_adult)
def meadultfavourites(request):
    return render(request, 'mepage/adult/favouritebooks.html')

@user_passes_test(is_adult)
def meAdultPossesses(request):
    possessBooks = request.user.adult.Adultposses.all()
    return render(request, 'mepage/adult/possessedbooks.html',{"possessBooks":possessBooks})

@user_passes_test(is_adult)
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



@user_passes_test(is_adult)
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

@user_passes_test(is_student)
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



@user_passes_test(is_student)
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


@login_required
def mestudentpossesses(request):
    possessBooks = request.user.student.Studentposses.all()
    return render(request, 'mepage/student/possessedbooks.html', {"possessBooks": possessBooks})


@user_passes_test(is_student)
def mestudent(request):
    return render(request, 'mepage/student/mepagestudent.html')

@user_passes_test(is_student)
def mestudentpossesses(request):
    possessBooks = request.user.student.Studentposses.filter(study_book=False)
    return render(request, 'mepage/student/possessedbooks.html', {"possessBooks": possessBooks})

@user_passes_test(is_student)
def mestudentevents(request):
    try:
        events = HomePage.objects.all()[0].events.all()
    except:
        events = None
    return render(request, 'mepage/student/events.html',{"events":events})


@user_passes_test(is_student)
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


@user_passes_test(is_student)
def mestudentlendedbooks(request):
    books=Book.objects.all()
    lendbooks= list(request.user.student.Studentposses.all())
    res=[]
    print(lendbooks)
    for book in lendbooks:
        if book.study_book==True:
            res.append(book)
    print(res)


    return render(request, 'mepage/student/lendedbooks.html',{"books": books,'lendbooks':res})

@user_passes_test(is_admin)
def meadminpage(request):
    if request.method == 'POST':
        print("imhere")
        students=Student.objects.all()
        for student in students:
            if student.grade != 12:
                student.grade+=1
                student.save()
    return render(request, 'mepage/admin/reports.html')



@user_passes_test(is_admin)
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


@user_passes_test(is_admin)
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
                    book.Take_Date=None
                    book.save()
            for user1 in Adult.objects.all():
                if book in user1.Adultposses.all():
                    user1.Adultposses.remove(book)
                    user1.save()
                    book.takenout = False
                    book.returned = True
                    book.posses = False
                    book.Take_Date = None
                    book.save()
    books = Book.objects.filter(returned=False)
    books = list(filter(lambda x:not x.returned,books))

    return render(request, 'mepage/admin/getin.html',{'books':books})


@user_passes_test(is_admin)
def damaged(request):
    if request.method == 'POST':
        id_list = request.POST.getlist('book.id')
        for bookid in id_list:
            book = get_object_or_404(Book, pk=bookid)
            book.Is_Damaged=False
            book.Damage_Description=None
            book.save()
    books = Book.objects.filter(Is_Damaged=True)
    return render(request, 'mepage/admin/damaged.html',{'books':books})


@user_passes_test(is_admin)
def delayed (request):
    books=Book.objects.all()
    temp=datetime.datetime.now()
    nowtime = datetime.date(temp.year, temp.month, temp.day)
    delayedbooks=[]
    for book in books:
        if book.Take_Date!=None:
            delta = nowtime-book.Take_Date
            if book.study_book:
                if delta.days>365:
                    students=Student.objects.all()
                    adults=Adult.objects.all()
                    for student in students:
                        if book in student.Studentposses.all():
                            delayedbooks.append((book, delta.days-365,student.user.username))
                    for adult in adults:
                        if book in adult.Adultposses.all():
                            delayedbooks.append((book, delta.days-365, adult.user.username))
            else:
                if delta.days>30:
                    students=Student.objects.all()
                    adults=Adult.objects.all()
                    for student in students:
                        if book in student.Studentposses.all():
                            delayedbooks.append((book, delta.days-30,student.user.username))
                    for adult in adults:
                        if book in adult.Adultposses.all():
                            delayedbooks.append((book, delta.days-30, adult.user.username))

    print(delayedbooks)
    return render(request, 'mepage/admin/delayed.html',{'books':delayedbooks})



@user_passes_test(is_admin)
def forumbanned (request):
    bannedstudents=Student.objects.filter(Forum_Banned=True)
    if request.method == 'POST':
        firstnames = request.POST.getlist('studentfirst')
        for firstname in firstnames:
            for student in bannedstudents:
                if student.user.first_name == firstname:
                    student.Forum_Banned=False
                    student.save()
                    bannedstudents = Student.objects.filter(Forum_Banned=True)
    return render(request, 'mepage/admin/forumbanned.html',{'students':bannedstudents})



@user_passes_test(is_admin)
def adultbanned (request):
    bannedadults=Adult.objects.filter(Is_Banned=True)
    if request.method == 'POST':
        firstnames = request.POST.getlist('adultfirst')
        for firstname in firstnames:
            for adult in bannedadults:
                if adult.user.first_name == firstname:
                    adult.Is_Banned=False
                    adult.save()
                    bannedadults=Adult.objects.filter(Is_Banned=True)
    return render(request, 'mepage/admin/adultbanned.html',{'adults':bannedadults})

def audobooks(request):
    books = AudioBook.objects.all()
    return render(request, "mepage/student/audiobooks.html",{"books":books})
