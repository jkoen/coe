# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-10-25 11:32
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('offering_request', '0004_auto_20161020_1527'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='offering_request',
            name='order_number',
        ),
        migrations.RemoveField(
            model_name='offering_request',
            name='status',
        ),
    ]
