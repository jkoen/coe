# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-10-20 15:25
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('offering_request', '0002_auto_20161020_1428'),
    ]

    operations = [
        migrations.AlterField(
            model_name='offering_request',
            name='request_date',
            field=models.DateField(default=datetime.date.today),
        ),
    ]
