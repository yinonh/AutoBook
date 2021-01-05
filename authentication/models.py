from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinLengthValidator
from book_catalog.models import Book




class Student(models.Model):
    user=models.OneToOneField(User, on_delete=models.SET_NULL,null=True,blank=True)
    grade=models.CharField(max_length=50,default=None)
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
    FavouriteBooks=models.ManyToManyField(Book,null=True,blank=True,related_name='favourite')
    Adultposses = models.ManyToManyField(Book, null=True, blank=True, related_name='adultposses')
    def __str__(self):
        return self.user.username
