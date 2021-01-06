from django.db import models
from django.contrib.auth.models import User

class Book (models.Model):
    name = models.CharField(max_length=50)
    author_name = models.CharField(max_length=50)
    summary = models.TextField(max_length=500)
    image = models.ImageField(upload_to='book_catalog/images', default='book_catalog/images/defult.png')
    #user_queue = NOT RELLEVANT YET
    available = models.BooleanField(default=True)
    librarian_favourite = models.BooleanField(default=False)
    #location =NOT RELLEVANT YET
    study_book = models.BooleanField(default=False)
    key_words =models.CharField(max_length=100)
    reader_name = models.CharField(max_length=50, blank=True)
    GENRE_CHOICES = (
        ('Drama','Drama'),('Roman','Roman'),
        ('Fantasy','Fantasy'),('Mystery','Mystery'),
        ('Poetry','Poetry'),('Short story','Short story'),
        ('Thriller','Thriller'),('Science fiction','Science fiction'),
        ('Horror', 'Horror'),('Fairytale','Fairytale'),
        ('Comic book', 'Comic book'), ('Adventure', 'Adventure'),
        ('Food', 'Food'),('Study Book', 'Study Book')
        )
    adult_only = models.BooleanField(default=False)
    kids = models.BooleanField(default=False)
    genre = models.CharField(default=True,max_length=100, choices=GENRE_CHOICES)
    posses = models.BooleanField(default=False)
    takenout = models.BooleanField(default=False)
    returned = models.BooleanField(default=True)
    Is_Damaged=models.BooleanField(default=False)
    Damage_Description=models.TextField(max_length=200,default=None,blank=True,null=True)
    # Grade_CHOICES = (
    #     (1, 1), (2, 2),(3, 3),(4, 4),(5, 5),(6, 6),(7, 7),(8, 8),(9, 9),(10, 10),(11, 11),(12, 12)
    # )
    # Grade = models.CharField(default=, max_length=100, choices=GENRE_CHOICES)


    def __str__(self):
        return self.name

