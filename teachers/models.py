from django.db import models


class Teacher(models.Model):
    title = models.CharField(max_length=150)
    description = models.TextField(max_length=500)
    Teacher_date = models.DateField(blank=True, null=True, default=None)