from django.test import TestCase


from django.test import RequestFactory, TestCase
# from django.utils.timezone import now
from django.contrib.auth.models import AnonymousUser, User

from .models import *
from .views import *

def allReview1(request, book_id):
    book = get_object_or_404(Book, pk=book_id)
    reviews = Review.objects.filter(book=book)
    rank, count = 0, 0
    for reviw in reviews:
        rank += reviw.rank
        count += 1
    reviews = []
    for review in Review.objects.all():
        if (book in review.book.all()):
            reviews.append(review)
    rank = rank / count if count > 0 else 0

    return render(request, "review/allReview.html", {"book": book,"reviews":reviews,"rank":rank})


class Reviewtest(TestCase):
    def test_setUp(self):
        Review.objects.create()
        rev=Review.objects.create(rank=5,title="dsgkn",text="dkgsj")
        rev.delete()

    def setUp(self):
        self.factory = RequestFactory()

    def test_allReview(self):
        request = self.factory.get('allReview1')
        abcde_book = Book.objects.create(name='abcde', author_name='temp', summary='temp', key_words='temp',
                                         genre='Fairytale',
                                         available=False, study_book=True,
                                         image='book_catalog/images/defult.png')
        response = allReview1(request,abcde_book.id)
        self.assertEqual(response.status_code, 200)
        self.assertNotEqual(response.status_code, 404)

