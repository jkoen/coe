# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-10-20 14:28
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('offering_request', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='offering_request',
            name='request_date',
            field=models.DateField(),
        ),
    ]
