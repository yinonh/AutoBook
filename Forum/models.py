from django.db import models
from authentication.models import Student
import datetime

class Forum(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    text = models.TextField(max_length=500)
    forumdate = models.DateField(default=datetime.datetime.now(), null=True, blank=True)

    def __str__(self):
        return self.title



class Comments(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    forum = models.ForeignKey(Forum, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    text = models.TextField(max_length=500)
    commentdate = models.DateField(default=datetime.datetime.now(), null=True, blank=True)

    def __str__(self):
        return self.title