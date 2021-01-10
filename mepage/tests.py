from django.test import TestCase

from django.test import RequestFactory, TestCase
from django.contrib.auth.models import AnonymousUser, User

from django.utils.timezone import now

from .views import *
from .models import *


def registerEvents1(request, event_id):
    event = get_object_or_404(Event, pk=event_id)
    if request.method == "POST":
        if "cancelled" in request.POST:
            event.registerstudent.remove(request.user.student)
        elif "register" in request.POST:
            event.registerstudent.add(request.user.student)

        event.save()
        return redirect("mestudentevents")
    return render(request, 'mepage/student/registerEvent.html', {"event": event})

def mestudentevents1(request):
    try:
        events = HomePage.objects.all()[0].events.all()
    except:
        events = None
    return render(request, 'mepage/student/events.html',{"events":events})

def mestudent1(request):
    return render(request, 'mepage/student/mepagestudent.html')

def meStudentReturn1(request, book_id):
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

def meStudentDamage1(request, book_id):
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

def meAdultDamage1(request, book_id):
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

def meAdultReturn1(request, book_id):
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
    return render(request, 'mepage/adult/meAdultReturn.html', {"book": book})

def meadultfavourites1(request):
    return render(request, 'mepage/adult/favouritebooks.html')


def meadminpage1(request):
    if request.method == 'POST':
        print("imhere")
        students=Student.objects.all()
        for student in students:
            if student.grade != 12:
                student.grade+=1
                student.save()
    return render(request, 'mepage/admin/reports.html')

def getout1(request):
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

def getin1(request):
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

def damaged1(request):
    if request.method == 'POST':
        id_list = request.POST.getlist('book.id')
        for bookid in id_list:
            book = get_object_or_404(Book, pk=bookid)
            book.Is_Damaged=False
            book.Damage_Description=None
            book.save()
    books = Book.objects.filter(Is_Damaged=True)
    return render(request, 'mepage/admin/damaged.html',{'books':books})


def delayed1(request):
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


class SignUptest(TestCase):
    def setUp(self):
        self.factory = RequestFactory()

    def test_meadultfavourites(self):
        request = self.factory.get('meadultfavourites1')
        response = meadultfavourites1(request)
        self.assertEqual(response.status_code, 200)
        self.assertNotEqual(response.status_code, 404)

    def test_meAdultReturn(self):
        request = self.factory.get('meAdultReturn1')
        abcde_book = Book.objects.create(name='abcde', author_name='temp', summary='temp', key_words='temp',
                                         genre='Fairytale',
                                         available=False, study_book=True,
                                         image='book_catalog/images/defult.png')
        response = meAdultReturn1(request,abcde_book.id)
        self.assertEqual(response.status_code, 200)
        self.assertNotEqual(response.status_code, 404)

    def test_meAdultDamage(self):
        request = self.factory.get('meAdultDamage1')
        abcde_book = Book.objects.create(name='abcde', author_name='temp', summary='temp', key_words='temp',
                                         genre='Fairytale',
                                         available=False, study_book=True,
                                         image='book_catalog/images/defult.png')
        response = meAdultDamage1(request,abcde_book.id)
        self.assertEqual(response.status_code, 200)
        self.assertNotEqual(response.status_code, 404)


    def test_meStudentDamage(self):
        request = self.factory.get('meStudentDamage1')
        abcde_book = Book.objects.create(name='abcde', author_name='temp', summary='temp', key_words='temp',
                                         genre='Fairytale',
                                         available=False, study_book=True,
                                         image='book_catalog/images/defult.png')
        response = meStudentDamage1(request,abcde_book.id)
        self.assertEqual(response.status_code, 200)
        self.assertNotEqual(response.status_code, 404)

    def test_meStudentReturn(self):
        request = self.factory.get('meStudentReturn1')
        abcde_book = Book.objects.create(name='abcde', author_name='temp', summary='temp', key_words='temp',
                                         genre='Fairytale',
                                         available=False, study_book=True,
                                         image='book_catalog/images/defult.png')
        response = meStudentReturn1(request,abcde_book.id)
        self.assertEqual(response.status_code, 200)
        self.assertNotEqual(response.status_code, 404)

    def test_mestudent(self):
        request = self.factory.get('mestudent1')
        response = mestudent1(request)
        self.assertEqual(response.status_code, 200)
        self.assertNotEqual(response.status_code, 404)

    def test_mestudentevents(self):
        request = self.factory.get('mestudentevents1')
        response = mestudentevents1(request)
        self.assertEqual(response.status_code, 200)
        self.assertNotEqual(response.status_code, 404)


    def test_registerEvents(self):
        request = self.factory.get('registerEvents1')
        event = Event.objects.create(title="adsg", text="dsjgh", date=now())
        response = registerEvents1(request,event.id)
        self.assertEqual(response.status_code, 200)
        self.assertNotEqual(response.status_code, 404)

    def test_meadminpage(self):
        request = self.factory.get('meadminpage1')
        response = meadminpage1(request)
        self.assertEqual(response.status_code, 200)
        self.assertNotEqual(response.status_code, 404)

    def test_getout(self):
        request = self.factory.get('getout1')
        response = getout1(request)
        self.assertEqual(response.status_code, 200)
        self.assertNotEqual(response.status_code, 404)

    def test_getin(self):
        request = self.factory.get('getin1')
        response = getin1(request)
        self.assertEqual(response.status_code, 200)
        self.assertNotEqual(response.status_code, 404)

    def test_damaged(self):
        request = self.factory.get('damaged1')
        response = damaged1(request)
        self.assertEqual(response.status_code, 200)
        self.assertNotEqual(response.status_code, 404)

    def test_delayed(self):
        request = self.factory.get('delayed1')
        response = delayed1(request)
        self.assertEqual(response.status_code, 200)
        self.assertNotEqual(response.status_code, 404)


