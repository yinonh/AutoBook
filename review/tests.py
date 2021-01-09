from django.test import TestCase
from teachers.models import Teacher

class Teachertest(TestCase):
    def test_setUp(self):
        Teacher.objects.create()

