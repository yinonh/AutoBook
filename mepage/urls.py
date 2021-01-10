from django.urls import path,include
from . import views
from . import tests
from teachers import views as teachersviews
from Activite_stud import views as Act_views
from teachers import tests as techersTest


urlpatterns = [
    path('Adult/', views.meadult, name="meadult"),
    path('Adult/Favourites/', views.meadultfavourites, name="meadultfavourites"),
    path('Adult/Possesses/', views.meAdultPossesses, name="meadultpossesses"),
    path('Adult/Possesses/<int:book_id>/', views.meAdultReturn, name="meAdultReturn"),
    path('Adult/Possesses/Damaged/<int:book_id>/', views.meAdultDamage, name="meAdultDamage"),
    path('Student/', views.mestudent, name="mestudent"),
    path('Student/Possesses/', views.mestudentpossesses, name="mestudentpossesses"),
    path('Student/Possesses/<int:book_id>/', views.meStudentReturn, name="meStudentReturn"),
    path('Student/Possesses/Damaged/<int:book_id>/', views.meStudentDamage, name="meStudentDamage"),
    path('Student/Events/', views.mestudentevents, name="mestudentevents"),
    path('Student/Activities/',Act_views.Activity_stud , name="activity"),
    path('Student/Events/<int:event_id>/', views.registerEvents, name="registerEvent"),
    path('Student/Teachers/', teachersviews.teachers, name="teachers"),
    path('Student/Teachers/<int:teacher_id>/', teachersviews.teachercard, name="teachercard"),
    path('Student/LendedBooks/', views.mestudentlendedbooks, name="melendedbooks"),
    path('Admin/Reports/', views.meadminpage, name="meadminpage"),
    path('getout/',views.getout,name="getout"),
    path('getin/',views.getin,name="getin"),
    path('damaged/',views.damaged,name="damaged"),
    path('delayed/',views.delayed,name="delayed"),
    path('forumbanned/',views.forumbanned,name="forumbanned"),
    path('adultsbanned/',views.adultbanned,name="adultbanned"),

    ###### test#######

    path('Student/Teachers/<int:teacher_id>/', techersTest.teachercard1, name="teachercard1"),
    path('Student/Teachers/', techersTest.teachers1, name="teachers1"),


    path('Student/Events/<int:event_id>/', tests.registerEvents1, name="registerEvent1"),
    path('Student/Events/', tests.mestudentevents1, name="mestudentevents1"),
    path('Student/', tests.mestudent1, name="mestudent1"),
    path('Student/Possesses/<int:book_id>/', tests.meStudentReturn1, name="meStudentReturn1"),
    path('Student/Possesses/Damaged/<int:book_id>/', tests.meStudentDamage1, name="meStudentDamage1"),
    path('Adult/Possesses/Damaged/<int:book_id>/', tests.meAdultDamage1, name="meAdultDamage1"),
    path('Adult/Possesses/<int:book_id>/', tests.meAdultReturn1, name="meAdultReturn1"),
    path('Adult/Favourites/', tests.meadultfavourites1, name="meadultfavourites1"),
    path('Admin/Reports/', tests.meadminpage1, name="meadminpage1"),
    path('getout/',tests.getout1,name="getout1"),
    path('getin/',tests.getin1,name="getin1"),
    path('damaged/',tests.damaged1,name="damaged1"),
    path('delayed/',tests.delayed1,name="delayed1"),


]