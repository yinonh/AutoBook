from django.test import RequestFactory, TestCase
from django.test import TestCase
from Activite_stud.models import Activity
from .views import Activity_stud

from django.utils import timezone
from django.utils.timezone import now
from django.contrib.auth.models import AnonymousUser, User


class Activitytest(TestCase):
    def test_setUp(self):
        Activity.objects.create()
        Activity.objects.create(title="gaa", grade= 3)
        self.factory = RequestFactory()

    def setUp(self):
        self.factory = RequestFactory()

    def test_Activity_stud(self):
        request = self.factory.get('activity')
        response = Activity_stud(request)
        self.assertEqual(response.status_code, 200)
        self.assertNotEqual(response.status_code, 404)




# Create your tests here.
