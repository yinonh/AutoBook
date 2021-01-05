from django.conf import settings
from django.urls import path,include
from review import views as viewReview
from . import views


urlpatterns = [
    path('', views.bookcataloge, name="bookcataloge"),
    path('<int:book_id>/', views.book_card, name="book_card"),
    path('<int:book_id>/review', viewReview.addReview, name="add_review"),


]