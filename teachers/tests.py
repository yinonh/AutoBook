from django.test import TestCase
from django.test import RequestFactory, TestCase
# from django.utils.timezone import now
from django.contrib.auth.models import AnonymousUser, User

from .models import *
from .views import *
# Create your tests here.

def teachers1(request):
    teachers1=Teacher.objects.all()
    teachers1 =teachers1.order_by('-Teacher_date')
    return render(request,'teachers/teachers.html',{'teachers':teachers1})

def teachercard1(request,teacher_id):
    teacher = get_object_or_404(Teacher, pk=teacher_id)
    return render(request,'teachers/teachercard.html',{'teacher':teacher})

class Teacherstest(TestCase):
    def test_setUp(self):
        tech=Teacher.objects.create(HourRate=5,title="dsgkn",description="dkgsj")
        Teacher.objects.create(HourRate=1, title="asdgahj", description="arh")
        tech.delete()

    def setUp(self):
        self.factory = RequestFactory()

    def test_teachers(self):
        request = self.factory.get('teachers1')
        response = teachers1(request)
        self.assertEqual(response.status_code, 200)
        self.assertNotEqual(response.status_code, 404)

    def test_teachercard(self):
        request = self.factory.get('teachercard1')
        tech = Teacher.objects.create(HourRate=1, title="asdgahj", description="arh")
        response = teachercard1(request,tech.id)
        self.assertEqual(response.status_code, 200)
        self.assertNotEqual(response.status_code, 404)
