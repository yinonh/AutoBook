from django.test import TestCase

from django.test import RequestFactory, TestCase
from django.contrib.auth.models import AnonymousUser, User


from django.contrib.auth.models import User
import datetime
from authentication.views import *
from authentication.models import *
from authentication.forms import *

class SignUptest(TestCase):
    def setUp(self):
        self.factory = RequestFactory()

    def test_signupuser(self):
        request = self.factory.get('signupuser')
        response = signupuser(request)
        self.assertEqual(response.status_code, 200)
        self.assertNotEqual(response.status_code, 404)

    def test_loginU(self):
        request = self.factory.get('loginU')
        response = loginU(request)
        self.assertEqual(response.status_code, 200)
        self.assertNotEqual(response.status_code, 404)

class Adulttest(TestCase):
    def setUp(self):
        self.factory = RequestFactory()

    def test_adultsignupuser(self):
        request = self.factory.get('adultsignupuser')
        response = adultsignupuser(request)
        self.assertEqual(response.status_code, 200)
        self.assertNotEqual(response.status_code, 404)

    def test_setUp(self):
        user = Adult.objects.create(
            ID_Number=123456789,
            Is_Banned=False,
            Security_Check=True,
        )
        self.factory = RequestFactory()
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

    def test_signup_adult(self):
        request = self.factory.get('/signup/student/')
        request.user = AnonymousUser()
        response = studentsignupuser(request)
        self.assertEqual(response.status_code, 200)




class Studenttest(TestCase):
    def setUp(self):
        self.factory = RequestFactory()

    def test_studentsignupuser(self):
        request = self.factory.get('studentsignupuser')
        response = studentsignupuser(request)
        self.assertEqual(response.status_code, 200)
        self.assertNotEqual(response.status_code, 404)

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

    def test_signup_student(self):
        request = self.factory.get('/signup/student/')
        request.user = AnonymousUser()
        response = studentsignupuser(request)
        self.assertEqual(response.status_code, 200)