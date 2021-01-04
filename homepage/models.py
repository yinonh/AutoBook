from django.db import models
from authentication.models import Student

class Event (models.Model):
    title = models.CharField(max_length=150)
    text = models.TextField(max_length=500)
    image = models.ImageField(upload_to='home/images', default='home/images/defult2.jpg')
    date = models.DateField()
    link = models.URLField(max_length=200,null=True,default=None,blank=True)
    registerstudent = models.ManyToManyField(Student, null=True, blank=True)



    def __str__(self):
        return self.title

class HomePage(models.Model):
    title = models.CharField(max_length=150)
    description = models.TextField(max_length=500)
    image = models.ImageField(upload_to='home/images', default='book_catalog/images/defult.png')
    events = models.ManyToManyField(Event, null=True, blank=True)
    change_Book_date = models.DateField(blank=True, null=True, default=None)

    def __str__(self):
        return self.title


