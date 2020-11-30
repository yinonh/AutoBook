# Generated by Django 3.1.3 on 2020-11-30 15:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book_catalog', '0004_auto_20201130_1724'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='genre',
            field=models.CharField(choices=[('Drama', 'Drama'), ('Roman', 'Roman'), ('Fantasy', 'Fantasy'), ('Mystery', 'Mystery'), ('Poetry', 'Poetry'), ('Short story', 'Short story'), ('Thriller', 'Thriller'), ('Science fiction', 'Science fiction'), ('Horror', 'Horror'), ('Fairytale', 'Fairytale'), ('Comic book', 'Comic book'), ('Adventure', 'Adventure'), ('Food', 'Food'), ('Study Book', 'Study Book')], default=True, max_length=100),
        ),
    ]
