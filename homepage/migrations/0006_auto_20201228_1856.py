# Generated by Django 3.1.3 on 2020-12-28 16:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0005_auto_20201228_1848'),
    ]

    operations = [
        migrations.AlterField(
            model_name='homepage',
            name='date',
            field=models.DateField(default=1),
        ),
    ]
