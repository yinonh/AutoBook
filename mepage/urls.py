from django.urls import path,include
from . import views
from Activite_stud import views as Act_views

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
    path('Student/LendedBooks/', views.mestudentlendedbooks, name="melendedbooks"),
    path('Admin/Reports/', views.meadminpage, name="meadminpage"),
    path('getout/',views.getout,name="getout"),
    path('getin/',views.getin,name="getin"),
    path('damaged/',views.damaged,name="damaged"),

]