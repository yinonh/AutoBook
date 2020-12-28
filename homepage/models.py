from django.db import models

class HomePage(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(max_length=400)
    link = models.URLField(blank=True)
    image = models.ImageField(upload_to='homepage/images/',default='book_catalog/images/defult.png')