# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-06-27 22:15
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('setForSummer_app', '0002_location_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='location',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
    ]
