# Generated by Django 4.1.4 on 2023-02-02 20:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("planner", "0003_alter_event_time"),
    ]

    operations = [
        migrations.AlterField(
            model_name="event",
            name="time",
            field=models.TimeField(null=True),
        ),
    ]
