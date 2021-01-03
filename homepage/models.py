from django.db import models

class Event (models.Model):
    title = models.CharField(max_length=150)
    text = models.TextField(max_length=500)
    image = models.ImageField(upload_to='book_catalog/images', blank=True)
    date = models.DateField()
    link = models.URLField(max_length=200,blank=True)