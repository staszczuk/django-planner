# Generated by Django 4.1.4 on 2023-01-14 01:00

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("planner", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="event",
            name="time",
            field=models.TimeField(default=datetime.time(0, 0)),
        ),
    ]
