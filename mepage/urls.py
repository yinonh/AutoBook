from django.urls import path,include
from . import views

urlpatterns = [
    path('Adult/', views.meadult, name="meadult"),
    path('Adult/Favourites/', views.meadultfavourites, name="meadultfavourites"),
    path('Adult/Possesses/', views.meadultpossesses, name="meadultpossesses"),
    path('Student/', views.mestudent, name="mestudent"),
    path('Student/Possesses/', views.mestudentpossesses, name="mestudentpossesses"),
    path('Student/Events/', views.mestudentevents, name="mestudentevents"),
    path('Student/LendedBooks/', views.mestudentlendedbooks, name="melendedbooks"),
    path('Admin/Reports/', views.meadminpage, name="meadminpage"),
    path('getout/',views.getout,name="getout")
]