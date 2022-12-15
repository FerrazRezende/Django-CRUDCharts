from datetime import datetime
from django.db import models


class Person(models.Model):          

    name = models.CharField(max_length=200, blank=True)
    email = models.CharField(max_length=500, blank=True)
    date = models.DateField(default=datetime.now, blank=True)
    gender = models.CharField(max_length=50, blank=True)

    def __str__(self):
        return self.name
