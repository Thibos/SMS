from __future__ import unicode_literals

from django.db import models
from django.utils import  timezone

# Create your models here.
class Event(models.Model):
    name = models.CharField(max_length=200)
    goal = models.IntegerField()
    sold  = models.IntegerField()
    deficit = models.IntegerField()
    created_date = models.DateTimeField(default=timezone.now)
    event_date = models.DateTimeField(blank=True,null=True)

    def __str__(self):
        return self.name
