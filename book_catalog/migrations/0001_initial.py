# Generated by Django 3.1.3 on 2020-11-29 16:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('book_id', models.IntegerField(max_length=9)),
                ('name', models.CharField(max_length=50)),
                ('author_name', models.CharField(max_length=50)),
                ('summary', models.CharField(max_length=300)),
                ('image', models.ImageField(upload_to='book_catalog/images')),
                ('available', models.BooleanField(default=True)),
                ('study_book', models.BooleanField(default=False)),
                ('key_words', models.CharField(max_length=100)),
                ('length', models.IntegerField(blank=True)),
                ('reader_name', models.CharField(blank=True, max_length=50)),
            ],
        ),
    ]
