# Generated by Django 3.1.3 on 2020-11-30 16:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('book_catalog', '0005_auto_20201130_1748'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='book',
            name='book_id',
        ),
    ]