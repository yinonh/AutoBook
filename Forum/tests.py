from django.test import TestCase

from django.test import RequestFactory, TestCase
from django.contrib.auth.models import AnonymousUser, User


from Forum.views import *
from Forum.models import *

class SignUptest(TestCase):
    def setUp(self):
        self.factory = RequestFactory()



# Create your tests here.
