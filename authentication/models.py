from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinLengthValidator
from book_catalog.models import Book
from review.models import Review



class Student(models.Model):
    user=models.OneToOneField(User, on_delete=models.SET_NULL,null=True,blank=True)
    Grade_CHOICES = (
        (1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6), (7, 7), (8, 8), (9, 9), (10, 10), (11, 11), (12, 12)
    )
    grade = models.IntegerField(default=1, max_length=100, choices=Grade_CHOICES, null=False, blank=False)
    type=models.CharField(max_length=50,default='Student')
    Forum_Banned=models.BooleanField(default=False)
    Phone_Number = models.CharField(max_length=10, validators=[MinLengthValidator(10)])
    Security_Check = models.BooleanField(default=False)
    Studentposses = models.ManyToManyField(Book, null=True, blank=True)

    def __str__(self):
        return self.user.username

class Adult(models.Model):
    user=models.OneToOneField(User, on_delete=models.SET_NULL,null=True,blank=True)
    ID_Number=models.CharField(max_length=9,default=None,validators=[MinLengthValidator(9)])
    type = models.CharField(max_length=50,default='Adult')
    Is_Banned = models.BooleanField(default=False)
    Security_Check = models.BooleanField(default=False)
    FavouriteBooks = models.ManyToManyField(Book, null=True, blank=True, related_name='favourite')
    Adultposses = models.ManyToManyField(Book, null=True, blank=True, related_name='adultposses')
    reviews = models.ManyToManyField(Review, null=True, blank=True)

    def __str__(self):
        return self.user.username
