# Generated by Django 3.1.3 on 2021-01-03 20:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book_catalog', '0020_book_returned'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='returned',
            field=models.BooleanField(default=True),
        ),
    ]
