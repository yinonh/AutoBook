from django.shortcuts import render, get_object_or_404, redirect
from review.forms import ReviewForm
from review.models import Review
from book_catalog.models import Book

def addReview(request, book_id):
    book = get_object_or_404(Book, pk=book_id)
    userReview = request.user.adult.reviews.filter(book=book)
    if request.method == "GET":
        if(len(userReview) > 0):
            return render(request, "review/addReview.html", {"form": ReviewForm(instance=userReview[0]), "book_id": book_id})
        else:
            return render(request, "review/addReview.html", {"form": ReviewForm(), "book_id": book_id})
    elif request.method == "POST":
        if(len(userReview) > 0):
            Review.delete(userReview[0])
        form = ReviewForm(request.POST)
        if form.is_valid():
            newReview = form.save(commit=False)
            newReview.save()
            newReview.book.add(book)
            request.user.adult.reviews.add(newReview)
            return redirect("homepage")
        else:
            return render(request, "review/addReview.html", {"form": ReviewForm(), "book_id": book_id,"error":"bad data"})



