from __future__ import unicode_literals

from django.db import models

# Create your models here.



class Customer(models.Model):
    username = models.CharField(max_length=31)
    Phone_Number = models.IntegerField()

    def __unicode__(self):
        return self.username
