# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2018-03-17 16:47
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurants', '0002_restaurants_location'),
    ]

    operations = [
        migrations.AlterField(
            model_name='restaurants',
            name='location',
            field=models.CharField(blank=True, max_length=120, null=True),
        ),
    ]
