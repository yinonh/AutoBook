# Generated by Django 3.1.3 on 2021-01-06 20:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0025_merge_20210105_2329'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='grade',
            field=models.IntegerField(choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6), (7, 7), (8, 8), (9, 9), (10, 10), (11, 11), (12, 12)], default=1, max_length=100),
        ),
    ]