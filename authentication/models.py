from django.db import models
from django.contrib.auth.models import User




class Student(models.Model):
    user=models.OneToOneField(User, on_delete=models.SET_NULL,null=True,blank=True)
    grade=models.CharField(max_length=50,default=None)
    type=models.CharField(max_length=50,default='Student')

    def __str__(self):
        return self.user.username

class Adult(models.Model):
    user=models.OneToOneField(User, on_delete=models.SET_NULL,null=True,blank=True)
    taz=models.CharField(max_length=10,default=None)
    type = models.CharField(max_length=50,default='Adult')

    def __str__(self):
        return self.user.username
