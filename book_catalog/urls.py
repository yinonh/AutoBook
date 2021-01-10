from django.conf import settings
from django.urls import path,include
from review import views as viewReview
from mepage import views as mePageView
from . import views
from review import tests


urlpatterns = [
    path('AudioBooks/', mePageView.audobooks, name="audobooks"),
    path('', views.bookcataloge, name="bookcataloge"),
    path('<int:book_id>/', views.book_card, name="book_card"),
    path('<int:book_id>/Review', viewReview.addReview, name="add_review"),
    path('<int:book_id>/AllReview', viewReview.allReview, name="all_review"),
    path('page/<int:page_num>', views.bookPage, name="bookPage"),

    path('<int:book_id>/AllReview', tests.allReview1, name="all_review1"),
]