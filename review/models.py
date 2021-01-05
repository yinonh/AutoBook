from django.db import models
from book_catalog.models import Book


class Review(models.Model):
    RANK_CHOICES = ((1, 1), (2, 2), (3, 3), (4, 4), (5, 5))
    rank = models.IntegerField(default=True, choices=RANK_CHOICES)
    title = models.CharField(max_length=50)
    text = models.TextField(max_length=200, default=None, blank=True, null=True)
    book = models.ManyToManyField(Book, null=True, blank=True)


    def __str__(self):
        return self.title
