from django.db import models
from datetime import datetime


class Taxi(models.Model):
    name = models.CharField(max_length=200)
    number = models.CharField(max_length=200)

    def __str__(self):
        return self.name + ' ' + self.number


class Driver(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100, unique=True)
    creation_date = models.DateTimeField('date published',
                                         default=datetime.now)
    password = models.CharField(max_length=200)
    taxi = models.OneToOneField(Taxi, on_delete=models.PROTECT)

    def __str__(self):
        return self.name