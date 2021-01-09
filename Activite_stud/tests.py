from django.test import TestCase
from Activite_stud.models import Activity

class Activitytest(TestCase):
    def test_setUp(self):
        Activity.objects.create()
        Activity.objects.create(title="gaa", grade= 3)


# Create your tests here.
