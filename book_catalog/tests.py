from django.test import TestCase
from book_catalog.models import Book, AudioBook

from django.test import RequestFactory, TestCase
from django.utils import timezone
from django.utils.timezone import now
from django.contrib.auth.models import AnonymousUser, User

from .views import *
from mepage.views import audobooks


class Booktest(TestCase):
    def setUp(self):
        self.factory = RequestFactory()

    def test_simple(self):
        request = self.factory.get('simple')
        response = simple(request)
        self.assertEqual(response.status_code, 200)
        self.assertNotEqual(response.status_code, 404)

    def test_home(self):
        request = self.factory.get('home')
        response = home(request)
        self.assertEqual(response.status_code, 200)
        self.assertNotEqual(response.status_code, 404)

    def test_bookcatalog(self):
        request = self.factory.get('bookcataloge')
        response = bookcataloge(request)
        self.assertEqual(response.status_code, 200)
        self.assertNotEqual(response.status_code, 404)

    def test_searchresults(self):
        request = self.factory.get('filteredbooks')
        response = filteredbooks(request)
        self.assertEqual(response.status_code, 200)
        self.assertNotEqual(response.status_code, 404)


    def test_setUp(self):
        Book.objects.create(name='hieexei',
                            author_name='jhcccs',
                            summary='dsjvvh',
                            key_words='ajsnnnh',
                            genre='Thriller',
                            available=True,
                            study_book=False,
                            image='book_catalog/images/defult.png')
        Book.objects.create(name='hieexei',
                            author_name='jhcccs',
                            image='book_catalog/images/defult.png')
        Book.objects.create(name='hieexei',
                            author_name='jhcccs')


    #All those next 5 checks are checking all lambdas functions from views.py's filteredbooks function
    def test_lambda1(self):
        books = Book.objects.all()
        Fairytalebook=Book.objects.create(name='RomanBook', author_name='temp', summary='temp', key_words='temp', genre='Fairytale',
                                available=True, study_book=False, image='book_catalog/images/defult.png')
        notFairytalebook=Book.objects.create(name='NotRomanBook', author_name='temp', summary='temp', key_words='temp', genre='Food',
                                available=True, study_book=False, image='book_catalog/images/defult.png')
        lambda1=list(filter(lambda x: x.genre == Fairytalebook.genre, books))
        result = lambda1
        self.assertEqual(result[0], Fairytalebook)

    def test_lambda2(self):
        books = Book.objects.all()
        abcde_book = Book.objects.create(name='temp', author_name='abcde', summary='temp', key_words='temp', genre='Fairytale',
                                            available=True, study_book=False,
                                            image='book_catalog/images/defult.png')
        abcd_book = Book.objects.create(name='temp', author_name='abcd', summary='temp',
                                               key_words='temp', genre='Food',
                                               available=True, study_book=False,
                                               image='book_catalog/images/defult.png')
        lambda2= list(filter(lambda x: abcd_book.author_name.lower() in x.author_name.lower(), books))
        result=lambda2
        self.assertEqual(result[0],abcde_book)

    def test_lambda3(self):
        books = Book.objects.all()
        abcde_book = Book.objects.create(name='abcde', author_name='temp', summary='temp', key_words='temp',
                                            genre='Fairytale',
                                            available=True, study_book=False,
                                            image='book_catalog/images/defult.png')
        abcd_book = Book.objects.create(name='abcd', author_name='temp', summary='temp',
                                               key_words='temp', genre='Food',
                                               available=True, study_book=False,
                                               image='book_catalog/images/defult.png')
        lambda3=list(filter(lambda x: abcd_book.name.lower() in x.name.lower(), books))
        result= lambda3
        self.assertEqual(result[0],abcde_book)

    def test_lambda4(self):
        abcde_book = Book.objects.create(name='abcde', author_name='temp', summary='temp', key_words='temp',
                                            genre='Fairytale',
                                            available=False, study_book=False,
                                            image='book_catalog/images/defult.png')
        abcd_book = Book.objects.create(name='abcd', author_name='temp', summary='temp',
                                               key_words='temp', genre='Food',
                                               available=True, study_book=False,
                                               image='book_catalog/images/defult.png')
        books = [abcd_book,abcde_book]
        lambda4 = list(filter(lambda x: x.available == True, books))
        result= lambda4
        self.assertEqual(result[0],abcd_book)

    def test_lambda5(self):
        abcde_book = Book.objects.create(name='abcde', author_name='temp', summary='temp', key_words='temp',
                                            genre='Fairytale',
                                            available=False, study_book=True,
                                            image='book_catalog/images/defult.png')
        abcd_book = Book.objects.create(name='abcd', author_name='temp', summary='temp',
                                               key_words='temp', genre='Food',
                                               available=True, study_book=False,
                                               image='book_catalog/images/defult.png')
        books = [abcd_book,abcde_book]
        lambda5 = list(filter(lambda x: x.study_book == True, books))
        result= lambda5
        self.assertEqual(result[0],abcde_book)

class AudioBooktest(TestCase):
    def setUp(self):
        self.factory = RequestFactory()


    def test_setUp(self):
        AudioBook.objects.create(name="Sdg", length=4, key_words="dfsd", genre='Study Book')
        AudioBook.objects.create(name="Sdg", length=4, key_words="dfsd", genre='Study Book')

    def test_audobooks(self):
        request = self.factory.get('audobooks')
        response = audobooks(request)
        self.assertEqual(response.status_code, 200)
        self.assertNotEqual(response.status_code, 404)

