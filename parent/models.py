from django.db import models
from datetime import datetime


class Parent(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100, unique=True)
    creation_date = models.DateTimeField('date published',
                                         default=datetime.now)
    password = models.CharField(max_length=200)

    def __str__(self):
        return self.name

