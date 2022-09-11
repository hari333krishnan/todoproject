import datetime
import time

from django.db import models

# Create your models here.

class Todo(models.Model):
    def __str__(self):
        return self.task
    task = models.CharField(max_length=100)
    priority = models.IntegerField()
    time = models.DateField(default=datetime.date.today())

