from django.shortcuts import render, get_object_or_404, redirect
from book_catalog.models import Book
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist
from authentication.models import Student,Adult
from homepage.models import Event,HomePage
from django.http import HttpResponse
from authentication.forms import AdultProfileForm,UserCreationForm,ExtendedUserCreationForm


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


    # if request.method=='POST' :
    #     # form2 = ExtendedUserCreationForm(request.POST,instance=request.user)
    #     form = AdultProfileForm(request.POST,instance=request.user)
    #     # print(user.adult.ID_Number)
    #     print(request.user.adult.ID_Number)
    #     if form.is_valid():
    #         # user=form2.save(commit=False)
    #         user1 = form.save(commit=False)
    #         print(request.user.adult.ID_Number)
    #         request.user.adult.ID_Number=user1.adult.ID_Number
    #         # user.set_password(form.cleaned_data['password'])
    #         user1.save()
    #         return redirect('meadult')
    # else:
    #         # form2 = ExtendedUserCreationForm(request.POST, instance=request.user)
    #         # print(user.adult.ID_Number)
    #         print(request.user.adult.ID_Number)
    #         form = AdultProfileForm(request.POST, instance=request.user)
    # return render(request, 'mepage/adult/mepageadult.html', {'form': form()})
# def edit_profile(request):
#     if request.method == 'POST':
#         form = EditProfileForm(request.POST, instance=request.user)
#         if form.is_valid():
#             user = form.save(commit=False)
#             user.set_password(form.cleaned_data['password'])
#             user.save()
#             return redirect('signupapp:profile')
#     else:
#         form=EditProfileForm(instance=request.user)
#     return render(request, "signupapp/edit_profile.html", {'form':form })


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
    try:
        events = HomePage.objects.all()[0].events.all()
    except:
        events = None
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
    # //lended = request.user.student.Studentlend.all()
    books=Book.objects.all()
    return render(request, 'mepage/student/lendedbooks.html',{"books": books})

    return render(request, 'mepage/student/possessedbooks.html', {"possessBooks": possessBooks})

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

