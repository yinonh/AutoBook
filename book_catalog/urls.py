from django.conf import settings
from django.urls import path,include
from review import views as viewReview
from . import views


urlpatterns = [
    path('', views.bookcataloge, name="bookcataloge"),
    path('<int:book_id>/', views.book_card, name="book_card"),
    path('<int:book_id>/Review', viewReview.addReview, name="add_review"),
    path('<int:book_id>/AllReview', viewReview.allReview, name="all_review"),
    path('page/<int:page_num>', views.bookPage, name="bookPage"),
]