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
    length = models.IntegerField(blank=True)
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
    genre = models.CharField(default=True,max_length=100, choices=GENRE_CHOICES)
    posses = models.BooleanField(default=False)
    takenout = models.BooleanField(default=False)
    Is_Damaged=models.BooleanField(default=False)

    def __str__(self):
        return self.name

