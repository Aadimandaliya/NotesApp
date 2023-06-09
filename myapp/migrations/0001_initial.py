# Generated by Django 4.1.5 on 2023-03-05 13:41

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='usersignup',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(blank=True, default=datetime.datetime(2023, 3, 5, 19, 11, 46, 978509))),
                ('firstname', models.CharField(max_length=20)),
                ('lastname', models.CharField(max_length=20)),
                ('username', models.CharField(max_length=30)),
                ('email', models.EmailField(max_length=254)),
                ('password', models.CharField(max_length=30)),
                ('city', models.CharField(max_length=20)),
                ('state', models.CharField(max_length=20)),
                ('mobile', models.BigIntegerField()),
            ],
        ),
    ]
