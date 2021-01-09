# Generated by Django 3.1.3 on 2021-01-07 16:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book_catalog', '0027_book_take_date'),
        ('review', '0006_auto_20210107_1759'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='review',
            name='book',
        ),
        migrations.AddField(
            model_name='review',
            name='book',
            field=models.ManyToManyField(blank=True, null=True, to='book_catalog.Book'),
        ),
    ]
