# Generated by Django 3.1.3 on 2020-11-30 21:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('book_catalog', '0010_book_librarianfavourite'),
    ]

    operations = [
        migrations.RenameField(
            model_name='book',
            old_name='librarianfavourite',
            new_name='librarian_favourite',
        ),
    ]
