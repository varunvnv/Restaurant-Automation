# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-17 02:23
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('placeorder', '0002_auto_20161116_1659'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='orderitem',
            name='menu_item_id',
        ),
        migrations.RemoveField(
            model_name='orderitem',
            name='order_id',
        ),
        migrations.AddField(
            model_name='order',
            name='menu_items',
            field=models.ManyToManyField(to='placeorder.MenuItem'),
        ),
        migrations.DeleteModel(
            name='OrderItem',
        ),
    ]
