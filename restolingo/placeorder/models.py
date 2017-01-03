"""
This file contains all the models that are used in our system
"""
from __future__ import unicode_literals

from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from autoslug import AutoSlugField
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User


# Create your models here.


class Employee(models.Model):
    username = models.CharField(max_length=31)
    password = models.TextField()
    role = models.IntegerField()

    def __unicode__(self):
        return self.username


class Table(models.Model):
    user_id = models.ForeignKey(User)
    slug = AutoSlugField(max_length=31,
                         unique=True,
                         null=True,
                         populate_from=str('id'),
                         help_text='A label for URL config.')
    status = models.CharField(max_length=10,
                              help_text='available - occupied - dirty') # the names should be available, occupied, dirty

    def __str__(self):
        return str(self.id)


class Item(models.Model):
    name = models.CharField(max_length=50)
    price = models.FloatField(default=0)
    type = models.CharField(max_length=30,help_text="snacks - desserts")
    slug = AutoSlugField(max_length=31,
                         unique=True,
                         null=True,
                         populate_from='name',
                         help_text='A label for URL config.')

    def __str__(self):
        return self.name


class Order(models.Model):
    user_id = models.ForeignKey(User)
    table_id = models.ForeignKey(Table)
    status = models.IntegerField(default=0)
    order_date = models.DateTimeField('date ordered',
                                      auto_now_add=True)
    items = models.ManyToManyField(Item, through='OrderItem')  # Many to many relationship is created automatically here
    slug = AutoSlugField(max_length=31,
                         unique=True,
                         null=True,
                         populate_from=str('order_date'),
                         help_text='A label for URL config.')
    total = models.FloatField(default=0)

    def get_absolute_url(self):
        return reverse('orders_detail',
                       kwargs={'slug': self.slug})

    def get_update_url(self):
        return reverse('make_order_in_progress',
                       kwargs={'slug': self.slug})

    def get_in_progress_url(self):
        return reverse('orders_detail',
                       kwargs={'slug': self.slug})

    def get_done_url(self):
        return reverse('make_order_done',
                       kwargs={'slug': self.slug})

    def __str__(self):
        return str(self.slug)


class OrderItem(models.Model):
    order_id = models.ForeignKey(Order, on_delete=models.CASCADE)
    item_id = models.ForeignKey(Item, on_delete=models.CASCADE)


class DynamicOrder(models.Model):
    item_name = models.CharField(max_length=50)
    cost = models.FloatField(default=0)
    table_id=models.ForeignKey(Table, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.item_name)

class Shift(models.Model):
    user_id = models.ForeignKey(User)
    start_date = models.DateTimeField('start_date')
    end_date = models.DateTimeField('end_date')

    def __str__(self):
        return str(self.id)
		
class OrderList(models.Model):
    order_id = models.ForeignKey(Order)
    item_name = models.ForeignKey(Item)
    table_id=models.ForeignKey(Table)
    status = models.IntegerField(default=1)
    def __str__(self):
        return str(self.id)
		

