from datetime import time

from django.db import models

# Create your models here.


class Event(models.Model):
    date = models.DateField()
    time = models.TimeField(null=True)
    name = models.CharField(max_length=128)

    def __str__(self):
        return self.name
