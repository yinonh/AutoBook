from django.db import models


class Activity(models.Model):
    title = models.CharField(max_length=150)
    grade_CHOICES = ((1, 1), (2, 2), (3, 3), (4, 4), (5, 5),(6,6),(7,7),(8,8),(9,9),(10,10),(11,11),(12,12))
    grade = models.IntegerField(default=True, choices=grade_CHOICES)
    link = models.URLField(max_length=200, null=True, default=None, blank=True)

# Create your models here.