from django.urls import path,include
from . import views
from teachers import views as teachersviews

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

]