# Generated by Django 3.2.13 on 2022-04-28 10:36

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo_app', '0002_alter_todo_task'),
    ]

    operations = [
        migrations.AddField(
            model_name='todo',
            name='time',
            field=models.DateField(default=datetime.date(2022, 4, 28)),
        ),
    ]
