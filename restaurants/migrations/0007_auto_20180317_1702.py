# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2018-03-17 17:02
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurants', '0006_restaurantlocation_timestamp'),
    ]

    operations = [
        migrations.AlterField(
            model_name='restaurantlocation',
            name='timestamp',
            field=models.DateTimeField(),
        ),
    ]
