# Generated by Django 3.1.3 on 2021-01-08 10:28

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Forum', '0005_auto_20210108_1223'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comments',
            name='commentdate',
            field=models.DateField(blank=True, default=datetime.datetime(2021, 1, 8, 12, 28, 15, 179361), null=True),
        ),
        migrations.AlterField(
            model_name='forum',
            name='forumdate',
            field=models.DateField(blank=True, default=datetime.datetime(2021, 1, 8, 12, 28, 15, 178364), null=True),
        ),
    ]
