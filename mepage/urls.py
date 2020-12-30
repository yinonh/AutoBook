from django.urls import path,include
from . import views

urlpatterns = [
    path('Me/Adult/', views.meadult, name="meadult"),
    path('Me/Adult/Favourites/', views.meadultfavourites, name="meadultfavourites"),
    path('Me/Adult/Possesses/', views.meadultpossesses, name="meadultpossesses"),
    path('Me/Student/', views.mestudent, name="mestudent"),
    path('Me/Student/Possesses/', views.mestudentpossesses, name="mestudentpossesses"),
    path('Me/Student/Events/', views.mestudentevents, name="mestudentevents"),
    path('Me/Student/LendedBooks/', views.mestudentlendedbooks, name="melendedbooks"),
]