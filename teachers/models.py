from django.db import models


class Teacher(models.Model):
    title = models.CharField(max_length=150)
    description = models.TextField(max_length=500)
    HourRate = models.IntegerField(null=True, default='25')

    About = models.TextField(max_length=500,null=True, default='None')
    Teacher_Name= models.CharField(max_length=40,null=True, default=None)
    Teacher_date = models.DateField(blank=True, null=True, default=None)
    METHOD_CHOICES = (
        ('Zoom', 'Zoom'), ('Frontal', 'Frontal'),
    )
    LessonMethod= models.CharField(default=True, max_length=100, choices=METHOD_CHOICES)