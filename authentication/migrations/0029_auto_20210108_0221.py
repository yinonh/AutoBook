# Generated by Django 3.1.3 on 2021-01-08 00:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book_catalog', '0028_auto_20210107_2204'),
        ('authentication', '0028_auto_20210108_0217'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='Studentposses',
            field=models.ManyToManyField(blank=True, to='book_catalog.Book'),
        ),
        migrations.AlterField(
            model_name='student',
            name='grade',
            field=models.IntegerField(choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6), (7, 7), (8, 8), (9, 9), (10, 10), (11, 11), (12, 12)], default=1),
        ),
    ]
