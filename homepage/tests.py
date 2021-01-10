from django.test import TestCase

from django.test import RequestFactory, TestCase
from django.utils import timezone
from django.utils.timezone import now
from django.contrib.auth.models import AnonymousUser, User
from django.utils.timezone import now

from .views import *
from .models import *

class HomePagetest(TestCase):
    def setUp(self):
        self.factory = RequestFactory()

    def test_setUp(self):
        HomePage.objects.create(title="asf",description="dsf")
        home = HomePage.objects.create(title="adsg", description="dsjgh")
        home.delete()

    def test_homepage(self):
        request = self.factory.get('homepage')
        response = homepage(request)
        self.assertEqual(response.status_code, 200)
        self.assertNotEqual(response.status_code, 404)

class Eventtest(TestCase):
    def setUp(self):
        self.factory = RequestFactory()

    def test_setUp(self):
        Event.objects.create(title="asf",text="dsf",date=now())
        event = Event.objects.create(title="adsg", text="dsjgh",date=now())
        event.delete()





# Create your tests here.
