from django.db import models

class Book (models.Model):
    book_id = models.IntegerField()
    name = models.CharField(max_length=50)
    author_name = models.CharField(max_length=50)
    summary = models.CharField(max_length=300)
    image = models.ImageField(upload_to='book_catalog/images')
    #user_queue =
    available = models.BooleanField(default=True)
    #location =
    study_book = models.BooleanField(default=False)
    key_words =models.CharField(max_length=100)
    #categories = models.Choices(names=Op)
    length = models.IntegerField(blank=True)
    reader_name = models.CharField(max_length=50, blank=True)

    def __str__(self):
        return self.name

