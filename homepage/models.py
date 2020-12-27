from django.db import models

class HomePage(models.Model):
    title=models.CharField(max_length=100)
    description=models.CharField(max_length=250)
    image=models.ImageField(upload_to='homepage/images/',default='book_catalog/images/defult.png')