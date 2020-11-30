from django.test import TestCase
from book_catalog.models import Book
"""import unittest
from book_catalog import views"""

class Booktest(TestCase):
    def test_setUp(self):
        Book.objects.create(name='hii',author_name='jhs',summary='dsjh',key_words= 'ajsh',length=5,genre= 'Roman',available= True, study_book = False,reader_name='sdkfjh',image= 'book_catalog/images/defult.png')
        Book.objects.create(name='hii', author_name='jhs', summary='dsjh', key_words='ajsh', length=5, reader_name='sdkfjh')
    #All those next 5 checks are checking all lambdas functions from views.py's filteredbooks function
    def test_lambda1(self):
        books = Book.objects.all()
        Fairytalebook=Book.objects.create(name='RomanBook', author_name='temp', summary='temp', key_words='temp', length=5, genre='Fairytale',
                                available=True, study_book=False, reader_name='temp', image='book_catalog/images/defult.png')
        notFairytalebook=Book.objects.create(name='NotRomanBook', author_name='temp', summary='temp', key_words='temp', length=5, genre='Food',
                                available=True, study_book=False, reader_name='temp', image='book_catalog/images/defult.png')
        lambda1=list(filter(lambda x: x.genre == Fairytalebook.genre, books))
        result = lambda1
        self.assertEqual(result[0], Fairytalebook)

    def test_lambda2(self):
        books = Book.objects.all()
        abcde_book = Book.objects.create(name='temp', author_name='abcde', summary='temp', key_words='temp',
                                            length=5, genre='Fairytale',
                                            available=True, study_book=False, reader_name='temp',
                                            image='book_catalog/images/defult.png')
        abcd_book = Book.objects.create(name='temp', author_name='abcd', summary='temp',
                                               key_words='temp', length=5, genre='Food',
                                               available=True, study_book=False, reader_name='temp',
                                               image='book_catalog/images/defult.png')
        lambda2= list(filter(lambda x: abcd_book.author_name.lower() in x.author_name.lower(), books))
        result=lambda2
        self.assertEqual(result[0],abcde_book)

    def test_lambda3(self):
        books = Book.objects.all()
        abcde_book = Book.objects.create(name='abcde', author_name='temp', summary='temp', key_words='temp',
                                            length=5, genre='Fairytale',
                                            available=True, study_book=False, reader_name='temp',
                                            image='book_catalog/images/defult.png')
        abcd_book = Book.objects.create(name='abcd', author_name='temp', summary='temp',
                                               key_words='temp', length=5, genre='Food',
                                               available=True, study_book=False, reader_name='temp',
                                               image='book_catalog/images/defult.png')
        lambda3=list(filter(lambda x: abcd_book.name.lower() in x.name.lower(), books))
        result= lambda3
        self.assertEqual(result[0],abcde_book)
    def test_lambda4(self):
        abcde_book = Book.objects.create(name='abcde', author_name='temp', summary='temp', key_words='temp',
                                            length=5, genre='Fairytale',
                                            available=False, study_book=False, reader_name='temp',
                                            image='book_catalog/images/defult.png')
        abcd_book = Book.objects.create(name='abcd', author_name='temp', summary='temp',
                                               key_words='temp', length=5, genre='Food',
                                               available=True, study_book=False, reader_name='temp',
                                               image='book_catalog/images/defult.png')
        books = [abcd_book,abcde_book]
        lambda4 = list(filter(lambda x: x.available == True, books))
        result= lambda4
        self.assertEqual(result[0],abcd_book)

    def test_lambda5(self):
        abcde_book = Book.objects.create(name='abcde', author_name='temp', summary='temp', key_words='temp',
                                            length=5, genre='Fairytale',
                                            available=False, study_book=True, reader_name='temp',
                                            image='book_catalog/images/defult.png')
        abcd_book = Book.objects.create(name='abcd', author_name='temp', summary='temp',
                                               key_words='temp', length=5, genre='Food',
                                               available=True, study_book=False, reader_name='temp',
                                               image='book_catalog/images/defult.png')
        books = [abcd_book,abcde_book]
        lambda5 = list(filter(lambda x: x.study_book == True, books))
        result= lambda5
        self.assertEqual(result[0],abcde_book)
