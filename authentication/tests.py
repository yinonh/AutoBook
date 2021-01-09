from django.test import TestCase
from authentication.models import Adult, Student
from django.contrib.auth.models import User
from book_catalog.models import Book
import datetime


class Adulttest(TestCase):
    def test_setUp(self):
        user = Adult.objects.create(
            ID_Number=123456789,
            Is_Banned=False,
            Security_Check=True,
        )
        user.delete()
        ####check if the user really deleted from the data base
        try:
            user = user.username
        except:
            pass
        else:
            raise Exception("user didnt deleted")
        user1 = Adult.objects.create(
            ID_Number=12345,
            Is_Banned=False,
            Security_Check=True,
        )
        user2 =Adult.objects.create(
            ID_Number=12345,
            Is_Banned=True,
            Security_Check=True,
        )
        if not user1.Security_Check == user2.Security_Check:
            raise Exception("error")

        user1.Security_Check = False

        if user1.Security_Check == user2.Security_Check:
            raise Exception("error")

class Studenttest(TestCase):
    def test_setUp(self):
        user = Student.objects.create(
            grade=2,
            Forum_Banned=True,
            Phone_Number=243,
            Security_Check=False
        )
        user.delete()
        ####check if the user really deleted from the data base
        try:
            user = user.username
        except:
            pass
        else:
            raise Exception("user didnt deleted")
        user1 = Student.objects.create(
            grade=2,
            Forum_Banned=True,
            Phone_Number=243,
            Security_Check=False
        )
        user2 = Student.objects.create(
            grade=4,
            Forum_Banned=True,
            Phone_Number=24342554732,
            Security_Check=False
        )
        if user1.Phone_Number >= user2.Phone_Number:
            raise Exception("data error")
        if user2.Security_Check != user1.Security_Check:
            raise Exception("data error")