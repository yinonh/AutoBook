# Generated by Django 3.1.3 on 2021-01-06 16:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150)),
                ('description', models.TextField(max_length=500)),
                ('About', models.TextField(default=None, max_length=500, null=True)),
                ('Teacher_Name', models.CharField(default=None, max_length=40, null=True)),
                ('Teacher_date', models.DateField(blank=True, default=None, null=True)),
            ],
        ),
    ]
