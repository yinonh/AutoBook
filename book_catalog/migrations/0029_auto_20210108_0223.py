# Generated by Django 3.1.3 on 2021-01-08 00:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book_catalog', '0028_auto_20210107_2204'),
    ]

    operations = [
        migrations.AlterField(
            model_name='audiobook',
            name='length',
            field=models.IntegerField(blank=True, default=None, null=True),
        ),
        migrations.AlterField(
            model_name='book',
            name='Grade',
            field=models.IntegerField(blank=True, choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6), (7, 7), (8, 8), (9, 9), (10, 10), (11, 11), (12, 12)], default=None, null=True),
        ),
    ]