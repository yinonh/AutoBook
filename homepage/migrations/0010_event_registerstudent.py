# Generated by Django 3.1.3 on 2021-01-03 19:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0021_auto_20201230_2207'),
        ('homepage', '0009_homepage'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='registerstudent',
            field=models.ManyToManyField(blank=True, null=True, to='authentication.Student'),
        ),
    ]