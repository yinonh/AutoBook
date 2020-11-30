from django.db import models

class Book (models.Model):
    book_id = models.IntegerField()
    name = models.CharField(max_length=50)
    author_name = models.CharField(max_length=50)
    summary = models.TextField(max_length=500)
    image = models.ImageField(upload_to='book_catalog/images')
    #user_queue =
    available = models.BooleanField(default=True)
    #location =
    study_book = models.BooleanField(default=False)
    key_words =models.CharField(max_length=100)
    #categories = models.Choices(names=Op)
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
    genre=models.CharField(default=True,max_length=100, choices=GENRE_CHOICES)

    def __str__(self):
        return self.name

