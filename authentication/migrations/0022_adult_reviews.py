# Generated by Django 3.1.3 on 2021-01-05 16:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('review', '0003_remove_review_user'),
        ('authentication', '0021_auto_20201230_2207'),
    ]

    operations = [
        migrations.AddField(
            model_name='adult',
            name='reviews',
            field=models.ManyToManyField(blank=True, null=True, to='review.Review'),
        ),
    ]
