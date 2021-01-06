from django.db import models


class Teacher(models.Model):
    title = models.CharField(max_length=150)
    description = models.TextField(max_length=500)
    About = models.TextField(max_length=500,null=True, default='None')
    Teacher_Name= models.CharField(max_length=40,null=True, default=None)
    Teacher_date = models.DateField(blank=True, null=True, default=None)