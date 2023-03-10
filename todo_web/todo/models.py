from django.db import models
from django.utils import timezone


import datetime


class AddTask(models.Model):
    task_id = models.IntegerField(primary_key=True)
    check_status = models.BooleanField(default=False)
    task = models.CharField(default='', max_length=200, blank=True)
    date = models.DateField(blank=True)
    time = models.TimeField(blank=True)

    def __str__(self):
        return self.task
