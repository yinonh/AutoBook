# Generated by Django 3.1.3 on 2020-12-28 18:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0010_remove_homepage_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='homepage',
            name='date',
            field=models.DateField(default=2),
            preserve_default=False,
        ),
    ]